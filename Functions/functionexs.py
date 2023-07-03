#functions without parameter
#calculating ones BMI

def calulateBMI():
    weight = float(input("Enter weight in kgs"))
    height = float(input("Enter height in meters"))
    BMI = weight / (height*height)
    print("Your BMI is", BMI)
calulateBMI()


#functions with parameters

def addnums(x , y):
    result = x+y
    print(result)

addnums(10 , 20)

#one that will display ones 2 names

def showname(first , last):
    print(first, last)
showname(input("Enter first name"), input("Enter last name"))