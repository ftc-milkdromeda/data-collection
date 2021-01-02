from dependancies import FileIO


def sort(indexOfElement, inputData):
    sortedData = []
    sortedData.append(data[0])
    for x in inputData[1:]:
        index = 0
        while index < len(sortedData) and sortedData[index][indexOfElement] <= x[indexOfElement]:
            index += 1
        sortedData.insert(index, x)

    return sortedData


data = []

next = False
while not next:
    fileName = input("Input file name: ")
    if input("\tConfirm (y/n): ").lower()[:1] == "y":
         next = True
data = FileIO.recall(fileName)

print("Starting sort")

data = sort(0, data)
sortedArray = []

index = 0
while index < len(data):
    upper = index + 1

    while upper < len(data) and data[index][0] == data[upper][0]:
        upper += 1

    for x in sort(1, data[index:upper + 1]):
        sortedArray.append(x)
    index = upper + 1

data = sortedArray

print("File saved as " + fileName + "-sorted")
FileIO.save(fileName + "-sorted", data)
