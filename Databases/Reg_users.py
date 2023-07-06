from Database import User

try:
    jina = input("Enter your Name\n")
    arafa = input("Enter your Email\n")
    siri = input("Enter your Password\n")

    User.create(name=jina, email=arafa, password=siri)
    print("User created successfully")

except:
    print("Failed to create user")
