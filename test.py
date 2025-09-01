# List operations in Python
''' fruit = ["apple", "banana", "cherry"]
print(fruit)
fruit.append("orange")
print(fruit)
print(fruit[3])
fruit[1] = "blackcurrant"
print(fruit)
fruit.remove("blackcurrant")
print(fruit)
print(len(fruit)) '''

# Tuple operations in Python
''' colors = ("red", "green", "blue")
print(colors)
print(colors[-1])
print(colors[1:3])
print(len(colors))
type(colors) '''

# Set operations in Python
''' animals = {"cat", "dog", "rabbit"}
print(animals)
animals.add("hamster")
print(animals) '''
# Dictionary operations in Python
''' person = {"name": "Raguram", "age": 32, "city": "Chennai"} 
print(person)
print(person["name"])
person["age"] = 33
print(person) '''

# Control flow in Python
''' amount = int(input("Enter the amount: "))
if amount == 300:
    print("You can buy a cake")
elif amount > 300:
    print("You can buy a cake+gift")
elif amount < 300 and amount >=200:
    print("You can buy a gift")
else:
    print("You cannot buy anything") '''
# Nested if-else 
''' amount = int(input("Enter the amount: "))
if amount >= 300:
    type = str(input("You can buy a cake or gift: "))
    if type == "cake":
        print("You can buy a cake")
    else:
        print("You can buy a gift")
else:
    print("You cannot buy anything") '''

# Looping in