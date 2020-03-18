import csv

"""
csv的追加写入
"""

with open('data.csv', 'a') as csvfile:
    fieldnames = ['id', 'name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writerow({'id': '10004', 'name': 'Durant', 'age': 22})