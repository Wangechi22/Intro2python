#calculating ones BMI

#weight = w
#height = h

weight = input("Enter w in kgs")
height = input("Enter h in meters")

w = float(weight)
h = float(height)

BMI= weight/(height*height)

print ("Your BMI is" , BMI)
if BMI <= 18:
    print ("Under weight")
elif 18.1 <= BMI <= 29:
    print ("Normal weight")
elif 29.1 <= BMI <= 34:
    print ("Over weight")
else:
    print ("Obese")

