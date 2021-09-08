import ast
import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = True if os.getenv('DEBUG') else False
USE_CERT = True  # Change to true after all production server API available
USE_TS = True

TIME_ZONE = os.getenv('TIME_ZONE')

CURRENT_CLINC = os.getenv('CURRENT_CLINIC')
CLINICS = ast.literal_eval(os.getenv('CLINICS'))
CLINIC_NAMES = ast.literal_eval(os.getenv('CLINIC_NAMES'))

API_URLS = ast.literal_eval(os.getenv('API_URLS'))
API_SECRET_KEYS = ast.literal_eval(os.getenv('API_SECRET_KEYS'))
INCOMING_API_SECRET_KEY = os.getenv('INCOMING_SECRET_KEY')

PFX_NAMES = ast.literal_eval(os.getenv('PFX_NAMES'))
PFX = {}
for clinic in PFX_NAMES:
    PFX[clinic] = os.getenv(PFX_NAMES[clinic])
CERT_PASS = os.getenv('CERT_PASS')