# Write a program that prints the numbers from 1 to 100.
# But for multiples of 3 print "Frizz"
# For multiples of 5 print "Buzz
# For multiples of both 3 & 5 print FrizzBuzz


lower = int(input("Enter lower range limit:"))
upper = int(input("Enter upper range limit:"))
for x in range(lower, upper + 1):
    if x % 3 == 0:
        print("Frizz")
    elif x % 5 == 0:
        print("Buzz")
    elif x % 3 == 0 & x % 5 == 0:
        print("Frizzbuzz")
    else:
        print(x)
