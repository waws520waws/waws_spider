import json

data = [{
    'name': '王伟',
    'gender': '男',
    'birthday': '1992-10-18'
}]

with open('data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))



"""
存在中文
with open('data.json', 'w') as file:
    file.write(json.dumps(data, indent=2))
[
  {
    "name": "\u738b\u4f1f",
    "gender": "\u7537",
    "birthday": "1992-10-18"
  }
]

解决方式：
with open('data.json', 'w', encoding='utf-8') as file:
    file.write(json.dumps(data, indent=2, ensure_ascii=False))
"""