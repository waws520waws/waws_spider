import json

"""
文件读取json内容
"""

with open('data.json', 'r') as file:
    str = file.read()
    data = json.loads(str)
    print(data)

