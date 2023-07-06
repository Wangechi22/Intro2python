#create another table in that database created
# Call it student
# It should have the following things: name of the student, phone number, age, gender and student code
# It should also have "student created successfully
# Display Students created in the db

from Database import *

class Student(Model):
    name = CharField()
    age = IntegerField()
    gender = CharField()
    student_code = IntegerField(unique=True)
    phone_number = IntegerField()

    class Meta:
        database = db

User.create_table(fail_silently=True)
