from dependancies import FileIO

data = []

def run():
    success = True
    next = False
    distance = input("\nInput a distance: ")
    if distance == "e":
        print()
        return

    power = input("Power fraction: ")

    active = True

    while active:
        s_success = input("Success (y/n): ")
        while not next:
            if s_success.lower()[:1] == "y":
                success = True
                next = True
            elif s_success.lower()[:1] == "n":
                success = False
                next = True
            elif s_success.lower()[:1] == "e":
                run()
                return
            else:
                s_success = input("Success (y/n): ")

        print(end="\n")
        print("Distance: " + str(distance))
        print("Power: " + str(power))
        print("Success: " + "Scored" if success else "Missed")

        confirm = input("\tConfirm (y/n): ")
        print("\n")
        if confirm.lower()[:1] == "n":
            continue

        data.append((distance, power, 1 if success else 0))
        next = False
    run()

active = True

while active:
    command = input("Input a command: ")
    if command == "save":
        name = input("Input file name to use: ")
        if input("\tConfirm (y/n): ").lower()[:1] == "n":
            continue
        FileIO.save(name, data)
    elif command == "exit":
        name = input("Input file name to use: ")
        if input("\tConfirm (y/n): ").lower()[:1] == "n":
            active = False
            continue
        FileIO.save(name, data)

        active = False
        continue
    elif command == "recall":
        data.clear()
        data = FileIO.recall(input("Enter file name: "))
        if input("\tConfirm (y/n): ").lower()[:1] == "n":
            continue
        else:
            if len(data) != 0:
                print("Recalled file!")
            else:
                print("Recall failed")
    elif command == "value":
            run()
    elif command == "print":
        iteration = 0
        for x in data:
            print(str(iteration), end=": ")
            print("Distance: " + str(x[0]), end=" ")
            print("Power: " + str(x[1]), end=" ")
            print("Success: " + str(x[2]))
            iteration += 1
    else:
        print("Unknown command, please try again.\t")

