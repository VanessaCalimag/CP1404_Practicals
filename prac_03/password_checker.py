
def main():

    password = input("Enter a password: ")
    while len(password) < 10:
        print("Minimum number of characters is 10 - Enter a password.")
        password = input("Enter a password: ")
    print('*' * len(password))


main()



