import csv
with open('tets1.csv', mode ='r')as file:
    csvFile = csv.reader(file)
    for lines in csvFile:
        print(lines)
