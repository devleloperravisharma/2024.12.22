# blueprint
# in object oriented programming, the class is the blueprint
#   --> all the classes will include features and functions
# all functions in a class will have the parameter "self"
class Student:
    # constructor function get executed by default
    # The purpose is to create and set the object properties
    # All of the 'self.[whatever]' are properties
    def __init__(self):
        self.name = ""
        self.age = ""
        self.school = "River Academy"
        self.grade = ""
        self.teacher = ""
        self.scores = []
    
    def change_detail(self):
        # we're changing the property values
        self.name = input("what is your name?    ")
        self.age = input("what is your age?    ")
        self.grade = input("what grade are you in?    ")
        self.teacher = input("who is your teacher?    ")
        subjects = int(input("how many subjects do you have?    "))
        for subject in range(1,subjects+1):
            marks = input(f"how many marks did you get in subject {subject}:    ")
            self.scores.append(marks)

    def display(self):
        print(f"-----\nREPORT CARD\nName of student: {self.name}\nAge of {self.name}: {self.age}\nGrade of {self.name}: {self.grade}\nTeacher of {self.name}: {self.teacher}\nNumber of subjects taken by {self.name}: {len(self.scores)}\nReport Card of{self.name}: {self.scores}")

    
# creating object

s1 = Student()
s2 = Student()
s1.change_detail()
s2.change_detail()
s1.display()
s2.display()
# the reason we don't put 's1.self.name' is because that s1 replaces the 'self'
print(s1.name)
print(s2.name)