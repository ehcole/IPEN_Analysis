import csv
import sys
data = list()
for line in sys.stdin:
    data.append(line)
with open("keffs.csv", 'w', newline = '') as csvfile:
    fieldnames = ['CB 1 % withdrawn', 'CB 2 % withdrawn', 'keff']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerow({'CB 1 % withdrawn' : "58.88", 'CB 2 % withdrawn' : "58.88", 'keff' : "1.00367"})
    for i in range(0, len(data), 3):
        writer.writerow({'CB 1 % withdrawn': data[i], 'CB 2 % withdrawn' : data[i + 1], 'keff' : data[i + 2]})
