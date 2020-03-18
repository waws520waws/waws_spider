
import json


"""
json写入文件，indent指定缩进
"""

data = [{
    'name': 'Bob',
    'gender': 'male',
    'birthday': '1992-10-18'
}]
with open('data.json', 'w') as file:
    file.write(json.dumps(data, indent=2))


"""
文件中的文本格式
[
  {
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
  }
]
"""