databasee=[{"username":"admin", "password":"admin"}
    ]

print("Welcome to the application:")

choice = int(input("""
Enter your choice
1. for login
2. for create account
>>"""))
for i in range(2):
    if choice == 1:
        usern = input("Enter your username:")
        passw = input("Enter your password:")
        user = dict(username = usern, password =passw)
        
        if user in databasee:
            print("Login successfully")
            cal = int(input(""" Enter
            1. for add
            2. sub"""))
        else:
            print("Invalid username or password")

    elif choice == 2:
        usern = input("Enter your username:")
        passw = input("Enter your password:")
        user = dict(username =usern, password = passw)
        if user in databasee:
            print("user aleardy exits") 
            
        else:
            databasee.append(user)
            print("Account created successfully")
            print(user)
            print(databasee)
    else:
        print("invalide choice")

print(databasee)
