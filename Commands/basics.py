import time
import operator
import re

username = ""

def set_username(name):
    global username
    username = name


def information(arguments):
    print(" ")
    print("Inception Shell")
    print("A shell running in a shell")
    print("Copyright (c) 2026 Justus Fischer")
    print(" ")


def help_information(arguments):
    print(" ")
    print("Available commands:")
    print("info")
    print("help")
    print("echo")
    print(" ")
    print("Not helpful at all - but later it will be!")
    print(" ")

def echo(arguments):
    try:
        if int(arguments[1]) > 500000:
            print("This are many many words...")
            print("Want to continute anyway? (y/n)")
            if str(input(username + ": ").lower()) == "n":
                return
        for i in range (int(arguments[1])):
            print(arguments[0])
        print(" ")
    except:
        try:
            print('Error: Invalid arguments "' + arguments[0] + '" and "' + arguments[1] + '"')
        except:
            print("Command uncomplete - Something was missing")
            print(" ")

def countTo(arguments):
    try:
        realTypo = arguments[0]
        if "." in arguments[0]:
            arguments[0] = arguments[0].replace(".", "")

        if "," in arguments[0]:
            arguments[0] = arguments[0].replace(",", "")

        if len(arguments) == 2 and  not arguments[1] == "":
            if arguments[1].lower() == "-y":
                if int(arguments[0]) > 2500000:
                    print("This is a big number and might take a while to count to")
                    print("Want to continute anyway? (y/n)")
                    if str(input(username + ": ")) == "n":
                        return
                start = time.time()
                for i in range (int(arguments[0])):
                    print(i)
                print("Counted to " + realTypo + " in " + str(round(time.time() - start, 2)) + " seconds")
                print(" ")
            else:
                print('Error: Invalid argument - Did you mean "-y"?')
                print(" ")
        else:
            if int(arguments[0]) > 500000000:
                print("This is a big number and might take a while to count to")
                print("Want to continute anyway? (y/n)")
                if str(input(username + ": ")) == "n":
                    return
            start = time.time()
            for i in range (int(arguments[0])):
                i = i
            print("Counted to " + realTypo + " in " + str(round(time.time() - start, 2)) + " seconds")
            print(" ")
    except:
        try:
            print('Error: Invalid argument "' + realTypo + '"')
        except:
            print("Command uncomplete - Something was missing")
        print(" ")


def exit_shell(arguments):
    print("Really want to exit? (y/n)")
    if str(input(username + ": ").lower()) == "y":
        print("Wow you really used the exit command - Impressing...")
        print("Have a nice day!")
        exit()


def calculator(arguments):

    operations = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv
    }

    try:
        if len(arguments) == 2:
            del arguments[1]


        for i in range (len(arguments)):
            arguments[i] = arguments[i].replace(" ", "")

        if len(arguments) < 2:
            arguments = re.split(r"([^\d.,])", arguments[0])

        firstNumber = float(arguments[0].replace(",", "."))
        firstmathsign = str(arguments[1])
        secondnumber = float(arguments[2].replace(",", "."))
        result = operations[firstmathsign](firstNumber, secondnumber)

        for i in range (int(len(arguments) - 3)):
            if i % 2 == 0:
                firstmathsign = str(arguments[i + 3])

            else:
                secondnumber = float(arguments[i + 3].replace(",", "."))
                result = operations[firstmathsign](result, secondnumber)

        print("Result: " + str(round(result, 2)))

    except:
        print("Error: Invalid arguments")