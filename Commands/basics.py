import time

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

        if len(arguments) == 2:
            if arguments[1] == "-y":
                start = time.time()
                for i in range (int(arguments[0])):
                    print(i)
                print("Counted to " + arguments[0] + " in " + str(round(time.time() - start, 2)) + " seconds")
                print(" ")
            else:
                print('Error: Invalid argument - Did you mean "-y"?')
                print(" ")
        else:
            start = time.time()
            for i in range (int(arguments[0])):
                i = i
            print("Counted to " + realTypo + " in " + str(round(time.time() - start, 2)) + " seconds")
            print(" ")
    except:
        try:
            print('Error: Invalid argument "' + arguments[0] + '"')
        except:
            print("Command uncomplete - Something was missing")
        print(" ")