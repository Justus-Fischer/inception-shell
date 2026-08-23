from Commands import dictionary as dic
import Commands as com

print("Welcome to the Inception Shell!")
print(" ")
username = str(input("Please enter a username: "))
com.set_username(username)
com.set_username2(username)
print(" ")
print(username + ": Type 'help' to get help")
print(" ")

while True:

    action = str(input(username + ": "))
    if len(action) < 2:
        continue
    action = action.split(" ")
    commandName = dic.get_command(action[0].lower())
    if commandName == None:
        print('Command "' + action[0] + '" not found')
    else:
        commandName(action[1:])