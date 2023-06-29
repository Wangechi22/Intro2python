# create as simple reward system where
# if user enters any number between 1-5
# they are rewarded

a = int(input("Input number"))

if a == 1:
    print("You've won 10,000")
elif a == 2:
    print("You've won 20,000")
elif a == 3:
    print("You've won 30,000")
elif a == 4:
    print("You've won 40,000")
elif a == 5:
    print("You've won 50,000")
else:
    print("Not valid")
