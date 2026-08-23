username = ""

def set_username2(name):
    global username
    username = name

def build_wordskyscraper(arguments):
    print(" ")
    try:

        if int(arguments[1]) > 100:
            print("This will be a huge skyscraper")
            print("Want to build anyway? (y/n)")
            if str(input(username + ": ").lower()) == "n":
                return
        text = arguments[0]
        height = int(arguments[1])

        ftext = str(text + " ")

        if arguments[2].lower() == "-v":

            length = len(ftext)
            number = height
            br = int(1)
            for i in range(height):
                print(" " * length * number + ftext * br)
                number = number - 1
                br = br + 2
            for i in range(height + height // 2):
                print(" " * length * number + ftext * br)

        elif arguments[2].lower() == "-h":
            number = int(0)
            for i in range(height):
                print(ftext * number)
                number = number + 1

            for i in range(height):
                print(ftext * number)
                number = number - 1

        else:
            print("Invalid argument. Use -v for vertical or -h for horizontal.")

        print(" ")

    except:
        try:
            print('Error: Invalid arguments "' + arguments[0] + '", "' + arguments[1] + '"and "' + arguments[2] + '"')
        except:
            print("Command uncomplete - Something was missing")
            print(" ")