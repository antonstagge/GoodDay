datafile = open("fakenews.dat", "r+")
positionfile = open("positions.dat", "r+")

def get_positions():
    positionfile.seek(0,0)
    str_positions = positionfile.readline().split(" ")
    positions = []
    for i in range(0,4):
        positions.append(int(str_positions[i]))

    return positions

def get_active_user(user):
    if (user == 'A' or user == 'a'):
        return 0
    elif (user == 'C' or user == 'c'):
        return 1
    elif (user == 'E' or user == 'e'):
        return 2
    elif (user == 'F' or user == 'f'):
        return 3
    else:
        print("not a valid user! Guest here maybe?")
        return -1

def get_active_pos(user):
    positions = get_positions()
    if (user != -1):
        return positions[user]
    else:
        return -1

def update_position(user_index, value):
    positions = get_positions()
    positions[user_index] = value
    positionfile.seek(0,0)
    newLine = ""
    for i in positions:
        newLine += str(i) + " "
    newLine += "\n"
    positionfile.writelines([newLine])


def main():
    char_user = input("Who's this? A = Anton, C = Crille, E = Erik, F = Fredde, rest = guest\n> ")
    user_index = get_active_user(char_user)
    active_pos = get_active_pos(user_index)
    print(active_pos)
    if active_pos == -1:
        datafile.seek(0, 2)
        datafile.write("\ntest")
    else:
        datafile.seek(active_pos, 0)
        answer = input("Did you have a good day? 1 = yes, 0 = no\n>")
        if (answer == '1' or answer == '0'):
            datafile.write(answer)
            update_position(user_index, -1)
        else:
            print("Not a valid answer to a good day question... bro...")
            return


main()

datafile.close()
positionfile.close()
