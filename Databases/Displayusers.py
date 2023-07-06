from Database import User

users = User.select()
#use a for loop to display the users

for user in users:
    print(user.name, user.email, user.password)


