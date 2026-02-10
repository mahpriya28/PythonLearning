#types of tuples
numbers=(1,2,3)
names=("Alice","Bob","Charlie")
status=(True,False,True)
data=(1,"Alice",True,3.14)
print(numbers,names, status, data)

#access elements of tuple -> by indexing
item=(10,)#single item tuple
print("item:", item)
print("item[0]:", item[0])
#negative indexing (accessing elemets from the end)
print("item[-1]:", item[-1])
fruits=("apple","banana","cherry","date")
print("fruits[1]:", fruits[1])
print("fruits[-2]:", fruits[-2])
#tuple slicing ()
print("fruits[0:2]:", fruits[0:2])
#fruits[0] = "grape" #tuples are immutable, cannot change elements
print(fruits.index("cherry")) #find index of an element
print(fruits.count("banana")) #count occurrences of an element
