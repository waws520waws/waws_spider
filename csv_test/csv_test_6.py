import csv


"""
尝试写入中文的时候，没有使用encoding='utf-8'，在文件中输出的是乱码，所以存在中文就要将
编码格式添加上去

"""
with open('data.csv', 'a', encoding='utf-8') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'id': '10005', 'name': '王伟', 'age': 22})