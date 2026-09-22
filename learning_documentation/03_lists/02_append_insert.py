#Start with a list. Do these three operations:
#1. append() Add "grape" at the end
#2. insert() Add "mango" at the start
#3. insert() Add "watermelon" in the index 2
#Then: 
#4. Print the entire list
#5. Print the element that is left in the index 2

fruits = ["apple", "banana", "orange"]
fruits.append("grape")
fruits.insert(0, "mango")
fruits.insert(2, "watermelon")
print(*fruits)
print(fruits[2])