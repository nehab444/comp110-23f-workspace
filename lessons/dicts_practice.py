"""Practice with dictionaries"""

#Constructing a dictionary
ice_cream: dict[str, int] = {"chocolate" :12, "vanilla" :8,"strawberry" :5}
print("Made my dictionary")
print(ice_cream)

#Adding a key, value pair to a dictionary
ice_cream["mint"] = 3
print("After adding mint:")
print(ice_cream)


#Removing a key, value pair from a dictionary
ice_cream.pop("mint")
print("After removing mint:")
print(ice_cream)

#View a key, value pair
print("Printing only number of chocolate orders:")
print(f"There are {ice_cream['chocolate']} orders of chocolate")

#Adjusting a value
print("Adjusting number of vanilla orders:")
ice_cream["vanilla"] = 10
print(ice_cream)

#Length of dict
print("How many kv pairs there are:")
print(len(ice_cream))

#Check if key is in dictionary
print("mint" in ice_cream)
print("chocolate" in ice_cream)

if "mint" in ice_cream:
    print(ice_cream["mint"])
else:
    print("no orders of mint")

#Use a for loop to print out how many values each key has

for key in ice_cream:
    print(f"{key} has {ice_cream[key]} orders")