import csv
import os

# def setColumnCount(operation):
#     if operation == 1:
#         dataColumns = 5
#     elif operation == 2:
#         dataColumns = 12
#     elif operation == 3:
#         dataColumns = 1
#     return dataColumns

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

#sensor data
def processSensorLog(filePath, nodeNumber):
    fileName = "SensorLog"
    fileExtension = ".txt"
    txtFile = fileName + fileExtension
    path = os.path.join(filePath, txtFile)
    columnCount = 12
    processor(path, fileName, columnCount, nodeNumber)

def processSensorLogFailedSend(filePath, nodeNumber):
    fileName = "SensorLogFailedSend"
    fileExtension = ".txt"
    txtFile = fileName + fileExtension
    path = os.path.join(filePath, txtFile)
    columnCount = 12
    processor(path, fileName, columnCount, nodeNumber)

def processSensorLogFailedPublish(filePath, nodeNumber):
    fileName = "SensorLogFailedPublish"
    fileExtension = ".txt"
    txtFile = fileName + fileExtension
    path = os.path.join(filePath, txtFile)
    columnCount = 12
    processor(path, fileName, columnCount, nodeNumber)

def processSensorLogPublished(filePath, nodeNumber):
    fileName = "SensorLogPublished"
    fileExtension = ".txt"
    txtFile = fileName + fileExtension
    path = os.path.join(filePath, txtFile)
    columnCount = 12
    processor(path, fileName, columnCount, nodeNumber)

#anemometer functions
def processIndoorAnemometerLog(filePath, nodeNumber):
    fileName = "IndoorAnemometerLog"
    fileExtension = ".txt"
    txtFile = fileName + fileExtension
    path = os.path.join(filePath, txtFile)
    columnCount = 5
    processor(path, fileName, columnCount, nodeNumber)

def processIndoorAnemometerLogFailedPublish(filePath, nodeNumber):
    fileName = "IndoorAnemometerLogFailedPublish"
    fileExtension = ".txt"
    txtFile = fileName + fileExtension
    path = os.path.join(filePath, txtFile)
    columnCount = 5
    processor(path, fileName, columnCount, nodeNumber)

def processIndoorAnemometerLogPublished(filePath, nodeNumber):
    fileName = "IndoorAnemometerLogPublished"
    fileExtension = ".txt"
    txtFile = fileName + fileExtension
    path = os.path.join(filePath, txtFile)
    columnCount = 5
    processor(path, fileName, columnCount, nodeNumber)

def processOutdoorAnemometerLog(filePath, nodeNumber):
    fileName = "OutdoorAnemometerLog"
    fileExtension = ".txt"
    txtFile = fileName + fileExtension
    path = os.path.join(filePath, txtFile)
    columnCount = 5
    processor(path, fileName, columnCount, nodeNumber)

def processOutdoorAnemometerLogFailedPublish(filePath, nodeNumber):
    fileName = "OutdoorAnemometerLogFailedPublish"
    fileExtension = ".txt"
    txtFile = fileName + fileExtension
    path = os.path.join(filePath, txtFile)
    columnCount = 5
    processor(path, fileName, columnCount, nodeNumber)

def processOutdoorAnemometerLogPublished(filePath, nodeNumber):
    fileName = "OutdoorAnemometerLogPublished"
    fileExtension = ".txt"
    txtFile = fileName + fileExtension
    path = os.path.join(filePath, txtFile)
    columnCount = 5
    processor(path, fileName, columnCount, nodeNumber)


nodeNumber = int(input("Enter node number: "))

isSink = isSinkNode()

fileDirectory = input(r"Enter file directory: ")

if isSink:
    #generate sensor data
    processSensorLog(fileDirectory, nodeNumber)
    processSensorLogFailedPublish(fileDirectory, nodeNumber)
    processSensorLogFailedSend(fileDirectory, nodeNumber)
    processSensorLogPublished(fileDirectory, nodeNumber)

    #generate anemometer data
    processIndoorAnemometerLog(fileDirectory, nodeNumber)
    processIndoorAnemometerLogFailedPublish(fileDirectory, nodeNumber)
    processIndoorAnemometerLogPublished(fileDirectory, nodeNumber)

    processOutdoorAnemometerLog(fileDirectory, nodeNumber)
    processOutdoorAnemometerLogFailedPublish(fileDirectory, nodeNumber)
    processOutdoorAnemometerLogPublished(fileDirectory, nodeNumber)
else:
    processSensorLog(fileDirectory, nodeNumber)
    processSensorLogFailedSend(fileDirectory, nodeNumber)