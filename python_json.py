import json
from collections import OrderedDict

# 딕셔너리 변수
data = {
    "Person" : {
"name" : "박대기", "age" : 30
}
}

# 딕셔너리 -> json
json_data = json.dumps(data, ensure_ascii=False,indent='\t')
print(json_data)

json_data2 = OrderedDict()
json_data2 = data

#딕셔너리 -> json 파일
with open("../Python_file_json/sample.json", 'w') as f:
    json.dump(data,f,ensure_ascii=False, indent = '\t')

#json 파일 -> 딕셔너리
with open("../Python_file_json/sample.json", 'r') as f:
    json_read_data = json.load(f)

#json 파일 -> str
with open("../Python_file_json/sample.json", 'r') as f:
    json_read_data2 = f.read()
    json.loads(json_read_data2)

print("\n읽기1(",type(json_read_data),") : ")
print(json_read_data)
print(json_read_data["Person"]["name"])

print("\n읽기2(",type(json_read_data2),") : ")
print(json_read_data2)
