try:
    with open('31test.txt') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")