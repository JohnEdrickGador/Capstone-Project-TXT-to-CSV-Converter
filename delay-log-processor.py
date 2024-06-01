import csv
import os

def csvMaker(entries, fileName, nodeNumber):
    fields = entries[0]
    csvFileName = f"{fileName}-Node-{nodeNumber}"
    saveDestination = r"D:\Documents\School\UP_Diliman\Fourth-year\Second-Semester\CoE-199\CSV-Files"
    directory = os.path.join(saveDestination,csvFileName)
    with open(directory, mode = "w", newline='') as csvfile:
        fieldNames = fields
        writer = csv.DictWriter(csvfile, fieldnames=fieldNames)
        writer.writeheader()

        for entry in entries[1::]:
            row = {fields[0]:entry[0]}
            writer.writerow(row)

def delayProcessor(filePath, fileName, columnCount, nodeNumber):
    file = open(filePath)
    entries = []

    if columnCount > 1:
        for line in file:
            data = line.strip().split(", ")
            entries.append(data)
        for entry in entries[1::]:
            for i in range(1, columnCount):
                try:
                    entry[i] = float(entry[i])
                except:
                    entry[i] = entry[i]
    elif columnCount == 1:
        for line in file:
            data = line.strip()
            entries.append([data])
        for entry in entries[1::]:
            for i in range(1, columnCount):
                try:
                    entry[i] = float(entry[i])
                except:
                    entry[i] = entry[i]
    file.close()

    csvMaker(entries, fileName, nodeNumber)
    print(f"Finished generating {fileName}-Node-{nodeNumber}")

def processDelayLog(filePath, nodeNumber):
    fileName = f"Node{nodeNumber}DelayLog"
    fileExtension = ".txt"
    txtFile = fileName + fileExtension
    path = os.path.join(filePath, txtFile)
    columnCount = 1
    delayProcessor(path, fileName, columnCount, nodeNumber)

nodeNumber = int(input("Enter node number: "))
fileDirectory = input(r"Enter file directory: ")

processDelayLog(fileDirectory, nodeNumber)