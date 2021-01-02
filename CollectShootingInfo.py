from dependancies import FileIO
from dependancies import prompts

data = []

def addData():
    prompts.printLine()
    print()

    distance = input("Input distance: ")
    power = input("Input power fraction: ")

    outcome = []

    active = True
    while active:
        outcome.append(input("Input outcome (1, 0, -1): "))

        if outcome[-1].lower()[0] == "e":
            del outcome[-1]
            active = False
            continue

        if not (outcome[-1] == "1" or outcome[-1] == "0" or outcome[-1] == "-1"):
            print("INVALID. Last entry void")
            del outcome[-1]

    print()

    for i in range(0, len(outcome)):
        print(str(i) + ": Distance: " + str(distance) + " Power: " + str(power) + " Outcome: " + str(outcome[i]))
        if prompts.confirm():
            data.append((float(distance), float(power), int(outcome[i])))

    prompts.printLine()
    print()

def manage():
    prompts.printLine()
    print()

    for i in range(0, len(data)):
        print(str(i) + ": Distance: " + str(data[i][0]) + " Power: " + str(data[i][1]) + " Outcome: " + str(data[i][2]))

    next = False
    while not next:
        print("\nType \"e\" to exit and \"d\" to modify.")
        command = input("\tCommand: ").lower()[0]

        if command == "e":
            next = True
        elif command == "d":
            print()
            index = input("Input index to delete: ")
            print(str(index) + ": Distance: " + str(data[int(index)][0]) + " Power: " + str(data[int(index)][1]) + " Outcome: " + str(data[int(index)][1]))
            if not prompts.confirm():
                continue
            del data[int(index)]
            for i in range(0, len(data)):
                print(str(i) + ": Distance: " + str(data[i][0]) + " Power: " + str(data[i][1]) + " Outcome: " + str(data[i][2]))

            print()

    prompts.printLine()
    print()

def help():
    pass

active = True
while active:
    command = input("Input a command: ")
    if command.lower() == "save":
        name = input("Input file name to use: ")
        if input("\tConfirm (y/n): ").lower()[:1] == "n":
            continue
        FileIO.save(name, data)

        print()
    elif command.lower() == "exit":
        name = input("Input file name to use: ")
        if input("\tConfirm (y/n): ").lower()[:1] == "n":
            active = False
            continue
        FileIO.save(name, data)

        active = False
        continue
    elif command.lower() == "recall":
        data.clear()
        data = FileIO.recall(input("Enter file name: "))
        if input("\tConfirm (y/n): ").lower()[:1] == "n":
            continue
        else:
            if len(data) != 0:
                print("Recalled file!")
            else:
                print("Recall failed")
            print()
    elif command.lower() == "add":
            addData()
    elif command.lower() == "manage":
        manage()
    elif command.lower() == "help":
        help()
    else:
        print("Unknown command, please try again.\n")

