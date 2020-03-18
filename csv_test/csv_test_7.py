import csv


"""
csv库读取csv文件
"""

with open('data.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)


"""
['id', 'name', 'age']
['10001', 'Mike', '20']
['10002', 'Bob', '22']
['10003', 'Jordan', '21']
['10004', 'Durant', '22']
['10005', '王伟', '22']
"""