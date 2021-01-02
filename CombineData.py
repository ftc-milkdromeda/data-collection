from dependancies import FileIO
from dependancies import prompts

fileNames = []

next = False
while not next:
    buffer = input("Enter file name: ")
    if prompts.confirm():
        fileNames.append(buffer)
        next = True

arrays = []
for fileName in fileNames:
    arrays.append(FileIO.recall(fileName))

output = []
for array in arrays:
    for dataPoint in array:
        output.append(dataPoint)

next = False
outputName = ""
while not next:
    outputName = input("New file name: ")
    True if prompts.confirm() else False

FileIO.save(outputName)
print("File saved")
