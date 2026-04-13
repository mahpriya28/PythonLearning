import csv
import json

file = open("example.txt", "r")
content = file.read()
print(content)
file.close()
file = open("example.txt", "w")
file.write("Hello, World!")
file.close()
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

with open("example.txt", "a") as file:
    file.write("\n Appended text!")
with open("example.txt", "r") as file:
    content = file.read()
    print(content)

with open("students.csv", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        if len(row) < 3:
            continue
        if row[0].strip().lower() == "name":
            continue
        name, age, score = row[0], row[1], row[2]
        print(f"Name: {name}, Age: {age}, Score: {score}")

with open("students.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Bob", "24", "55"])

with open("data.json", "r") as file:
    data = json.load(file)
    print(data)
    print(data["name"])
    print(data["contact"]["email"])

data = {
    "name": "Bob Smith",
    "age": 30,
    "city": "New York",
    "contact": {
        "email": "bob.smith@example.com",
        "phone": "123-456-7800"
    }
}

with open("data.json", "a") as file:
    json.dump(data, file, indent=4)