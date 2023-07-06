from Assignment import Student

try:
    jina = input("Enter your Name\n")
    miaka = input("Enter your Age\n")
    jinsia = input("Enter your Gender\n")
    codi = input("Enter your student code\n")
    nambari_ya_simu = input("Enter your phone number\n")

    Student.create(name=jina, miaka=age, jinsia=gender, codi=student_code, nambari_ya_simu=phone_number)
    print("Student created successfully")

except:
    print("Failed to create student")
