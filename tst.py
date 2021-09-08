import json
from array import array


array_data = {"patientno":"1111111","order":[{"type":"rp","detail":{"code":"12345678","name":"xxxxxx","qty":1}},{"type":"iv","detail":{"code":"12345678","name":"xxxxxx","qty":1,"type":1}},{"type":"doc","detail":{"code":"12345678","name":"xxxxxx","qty":1}},{"type":"jihi_other","detail":{"code":"12345678","name":"xxxxxx","qty":1}},{"type":"txt","detail":"xxxxxxxxxxxx"}]}
json_data = json.dumps(array_data, indent=4, ensure_ascii=False)
print(json_data)