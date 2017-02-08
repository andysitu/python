#! python3
# removeCsvHeader.py - removes the header from all csv files in the current
# directory.

import csv, os

os.makedirs('headerRemoved', exist_ok=True)

#Loop through every file in the current working directory
for csvFilename in os.listdir('.'):
    if no csvFilename.endswith('csv'):
        continue

    print('Removing header from ' + csvFilename)

    csvRows = []
    csvFileObj = open(csvFilename)
    readerObj = csv.reader(csvFileObj)
    for row in readerObj:
        if readerObj.line_num == 1:
            continue
        csvRows.append(row)
    csvFileObj.close()

    csvFileObj = open(os.path.join('headerRemoved', csvFilename), 'w', newline='')
    csvWriter = csv.writer(csvFileObj)
    for row in csvRows:
        csvWriter.writerow(row)
    csvFileObj.close()
