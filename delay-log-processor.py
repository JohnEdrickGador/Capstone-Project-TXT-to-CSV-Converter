import csv
import os

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
    else:
        for line in file:
            data = line.strip()
            entries.append(data)
        for entry in entries[1::]:
            for i in range(1, columnCount):
                try:
                    entry[i] = float(entry[i])
                except:
                    entry[i] = entry[i]
    file.close()

    
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