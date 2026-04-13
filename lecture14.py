class Student:
    def __init__(__self__, name, age):
        __self__.name = name
        __self__.age = age
    name="Priya"
    age="20"
    def greet(__self__):
        print("Hello, I am a student.")
        print(__self__.age)

s1=Student("Priya Mah",23)
s2=Student("Priya Maheshwary",24)
print(s1.name)
print(s2.name)
print(s1.greet())
print(s2.greet())