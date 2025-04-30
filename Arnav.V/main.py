#fix login issue
#make change password function

def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Quit")

        try:
            option = int(input("Enter choice: "))
            if option == 1:
                register()
            elif option == 2:
                login()
            elif option == 3:
                quit()
            else:
                print("Invalid option")
        except ValueError:
            print("Please enter a valid number.")

        main()

def register():
    name = input("What's your name? ")
    password = input("What's your password? ")

    with open("user&pass.txt", "a") as file:
    	file.write(f"{name},{password}\n")

    print("Registered!")
    main()
    return

def login():
    name_login = input("Enter username: ")
    password_login = input("Enter password: ")
    
    with open("user&pass.txt", "r") as file:
        for line in file:
            username, password = line.strip().split(",")
            if name_login == username and password_login == password:
                print("Logged in!")
                logged_in()
            else:
                print("Incorrect password or username")
                login()
        

def logged_in():
    print("1. Logout")
    print("2. Change password")
    choice = int(input("Enter choice: "))
    if choice == 1:
        quit()
    elif choice == 2:
        change_password()

def quit():
    exit()

def change_password():
    name = input("Enter your username: ")
    old_password = input("Enter your old password: ")
    new_password = input("Enter your new password: ")

    lines = []
    with open("user&pass.txt", "r") as file:
        for line in file:
            username, password = line.strip().split(",")
            if username == name and password == old_password:
                lines.append(f"{username},{new_password}\n")
            else:
                lines.append(line)

    with open("user&pass.txt", "w") as file:
        file.writelines(lines)

    print("Password changed successfully!")

main()
#   with open("user&pass.txt" "w") as file:
#       for line in file:
#           new_password = password