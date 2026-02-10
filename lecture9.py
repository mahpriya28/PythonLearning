#dicts -> stores data in key:value pairs
#dictionaries are mutable (can be changed)
#dictionaries are unordered (no index)
#dictionaries are defined using curly braces {}
#keys must be unique and immutable (strings, numbers, tuples)
#values can be of any data type and can be duplicated

#types of dictionaries
#1. standard dictionary
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

#2. nested dictionary
my_nested_dict = {
    "person1": {
        "name": "Bob",
        "age": 25
    },
    "person2": {
        "name": "Charlie",
        "age": 35
    }
}
#3. dictionary with mixed data types
my_mixed_dict = {
    "name": "David",
    "age": 40,
    "hobbies": ["reading", "traveling"],
    "is_student": False
}
#accessing values in a dictionary
print(my_dict["name"])  # Output: Alice
print(my_nested_dict["person1"]["age"])  # Output: 25
print(my_mixed_dict["hobbies"][0])  # Output: reading
#modifying values in a dictionary
my_dict["age"] = 31
print(my_dict["age"])  # Output: 31
my_nested_dict["person2"]["name"] = "Charlie Brown"
print(my_nested_dict["person2"]["name"])  # Output: Charlie Brown
my_mixed_dict["is_student"] = True
print(my_mixed_dict["is_student"])  # Output: True

#adding new key-value pairs
my_dict["country"] = "USA"
print("city is: ", my_dict.get("state"))
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'city': 'New York', 'country': 'USA'}
my_nested_dict["person3"] = {"name": "Eve", "age": 28}
print(my_nested_dict)  # Output: {'person1': {'name': 'Bob', 'age': 25}, 'person2': {'name': 'Charlie Brown', 'age': 35}, 'person3: {'name': 'Eve', 'age': 28}}
my_mixed_dict["favorite_color"] = "blue"
print(my_mixed_dict)  # Output: {'name': 'David', 'age': 40, 'hobbies': ['reading', 'traveling'], 'is_student': True, 'favorite_color': 'blue'}

#removing key-value pairs
del my_dict["city"]
print(my_dict)  # Output: {'name': 'Alice', 'age': 31, 'country': 'USA'}
my_nested_dict.pop("person1")
print(my_nested_dict)  # Output: {'person2': {'name': 'Charlie Brown', 'age': 35}, 'person3': {'name': 'Eve', 'age': 28}}
my_mixed_dict.pop("hobbies")
print(my_mixed_dict)  # Output: {'name': 'David', 'age': 40, 'is_student': True, 'favorite_color': 'blue'}

print(my_dict.keys(), my_dict.values(), my_dict.items())

for key in my_dict:
    print(key)

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)