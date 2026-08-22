from Commands import dictionary as dic

print("Welcome to the Inception Shell!")
print(" ")
username = str(input("Please enter a username: "))
print(" ")
print(username + ": Type 'help' to get help")
print(" ")

while True:

    action = str(input(username + ": "))
    if len(action) < 2:
        continue
    action = action.lower().split(" ")
    commandName = dic.get_command(action[0])
    if commandName == None:
        print('Command "' + action[0] + '" not found')
    else:
        commandName(action[1:])