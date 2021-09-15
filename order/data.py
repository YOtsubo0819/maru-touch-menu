from . import config
import time
import json
import base64
import contextlib
import hashlib
import requests
# import arrow
from io import BytesIO
import OpenSSL.crypto
import tempfile


@contextlib.contextmanager
def pfx_to_pem(pfx_bytes, pfx_password):
    """
    Decrypts the .pfx file to be used with requests.
    """
    with tempfile.NamedTemporaryFile(suffix='.pem') as t_pem:
        f_pem = open(t_pem.name, 'wb')
        pfx = pfx_bytes.getvalue()
        p12 = OpenSSL.crypto.load_pkcs12(pfx, pfx_password.encode('utf-8'))
        f_pem.write(OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, p12.get_privatekey()))
        f_pem.write(OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, p12.get_certificate()))
        ca = p12.get_ca_certificates()
        if ca is not None:
            for cert in ca:
                f_pem.write(OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, cert))
        f_pem.close()
        yield t_pem.name


@contextlib.contextmanager
def pfx_to_pem_bytes(pfx_bytes, pfx_password):
    """
    Decrypts and transfers the .pfx file to be used with requests.
    """
    f_pem = BytesIO()
    pfx = pfx_bytes.getvalue()
    p12 = OpenSSL.crypto.load_pkcs12(pfx, pfx_password.encode('utf-8'))
    f_pem.write(OpenSSL.crypto.dump_privatekey(OpenSSL.crypto.FILETYPE_PEM, p12.get_privatekey()))
    f_pem.write(OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, p12.get_certificate()))
    ca = p12.get_ca_certificates()
    if ca is not None:
        for cert in ca:
            f_pem.write(OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_PEM, cert))
    return f_pem
    # * Waiting for a potential Python update (psf/requests needs update too) to add the feature...
    # ...of support to file-like objects to make this function useful rather than the above one
    # * It has been a problem since year 2012 (nearly a decade)
    # * It was a core level issue according to issue 16487
    # Related:
    # https://bugs.python.org/issue16487
    # https://github.com/python/cpython/pull/2449
    # https://github.com/psf/requests/issues/4032


def make_request(patient_data,
                 clinic_id: str,
                 printurl=True,
                 ):

    data = json.dumps(patient_data, ensure_ascii=False)
    """
    Make requests to KARTE API
    """
    api_url = config.API_URLS[clinic_id]
    secretkey = config.API_SECRET_KEYS[clinic_id]
    ts = str(int(time.time()))
    string = str(secretkey) + str(config.CURRENT_CLINC) + ts
    token =  hashlib.md5(string.encode('utf-8')).hexdigest()
    params = {
        #'clinic': clinic_id,
        'token': token,
        'ts': ts,
    }
    pfx_key_buffer = BytesIO(base64.b64decode(config.PFX[clinic_id]))
    with pfx_to_pem(pfx_key_buffer, config.CERT_PASS) as cert:
        r = requests.post(api_url.strip('\''), cert=cert, params=params ,data=data.encode('utf-8'))
    if printurl:
        print(r.url)
    try:
        return print(r.json())
    except json.decoder.JSONDecodeError:
        return {}
