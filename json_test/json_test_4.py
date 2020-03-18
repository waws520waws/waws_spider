import json


"""
json写入文件
json.dumps()会自动将json串中的单引号变成双引号
"""

data = [{
    'name': 'Bob',
    'gender': 'male',
    'birthday': '1992-10-18'
}]
with open('data.json', 'w') as file:
    file.write(json.dumps(data))