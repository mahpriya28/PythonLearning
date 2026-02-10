numbers={1,2,3,3,4,5}
print(numbers, type(numbers))
#types of sets
names={"Alice", "Bob", "Charlie"}
status={True, False, True}
data={1, "Hello", 3.14, True}
empty_set=set()
print("Set of names:", names)
print("Set of status:", status)
print("Set of mixed data types:", data)
print("Empty set:", empty_set)
#empty_set1={}
#print("Empty set:", empty_set1)

#sets are changeable
fruits={"apple", "banana", "cherry"}
fruits.add("orange")
print("Fruits after adding orange:", fruits)
fruits.remove("banana")
print("Fruits after removing banana:", fruits)
fruits.discard("grape")  # No error if grape is not found
print("Fruits after discarding grape:", fruits)
fruits.clear()
print("Fruits after clearing:", fruits)

a={1,2,3}
b={3,4}
#union of sets
print("union: ", a|b)
#intersection of sets
print("intersection: ",a&b)
#difference of sets
print("difference: ",b-a)

for item in a :
    print(item)