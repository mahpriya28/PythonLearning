class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    name="Priya"
    age="20"
    def greet(self):
        print("Hello, I am a student.")

s1=Student("Priya Mah",23)
s2=Student("Priya Maheshwary",24)
print(s1.name)
print(s2.name)
print(s1.greet(), s2.greet())