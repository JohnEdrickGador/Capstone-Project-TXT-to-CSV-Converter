import csv
import os

def setColumnCount(operation):
    if operation == 1:
        dataColumns = 5
    elif operation == 2:
        dataColumns = 12
    elif operation == 3:
        dataColumns = 1
    return dataColumns

def isSinkNode():
    isSink = input("Is the node a sink node: ")
    if isSink in ["y", "Y"]:
        return True
    elif isSink in ["n", "N"]:
        return False
    
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
            row = {field: entry[i] for i, field in enumerate(fieldNames)}
            writer.writerow(row)

def processor(filePath, fileName, columnCount,nodeNumber):
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
    file.close()

    csvMaker(entries, fileName, nodeNumber)
    print(f"Finished generating {fileName}-Node-{nodeNumber}")

def processSensorLog(filePath, columnCount, nodeNumber):
    fileName = "SensorLog"
    fileExtension = ".txt"
    txtFile = fileName + fileExtension
    path = os.path.join(filePath, txtFile)
    processor(path, fileName, columnCount, nodeNumber)

def processSensorLogFailedSend(filePath, columnCount, nodeNumber):
    fileName = "SensorLogFailedSend"
    fileExtension = ".txt"
    txtFile = fileName + fileExtension
    path = os.path.join(filePath, txtFile)
    processor(path, fileName, columnCount, nodeNumber)

def processSinkNode(filePath):
    return True

nodeNumber = int(input("Enter node number: "))

operation = int(input(
'''What are you going to process?
1 - Anemometer Data
2 - Sensor Data
3 - Latency Data
'''))

columnCount = setColumnCount(operation)
isSink = isSinkNode()

fileDirectory = input(r"Enter file directory: ")

processSensorLog(fileDirectory, columnCount, nodeNumber)