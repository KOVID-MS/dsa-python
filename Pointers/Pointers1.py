
dict1 = {
            "value":11
        }

dict2 = dict1

print("Before changing the value of dict2")

print("\ndict1 holds the value ", dict1)
print("dict2 holds the value ", dict2)

print("dict1 points to ", id(dict1))
print("dict2 points to ", id(dict2))


dict2["value"] = 22

print("\nAfter changing the value of dict2")
print("\ndict1 holds the value ", dict1)
print("dict2 holds the value ", dict2)

print("dict1 points to ", id(dict1))
print("dict2 points to ", id(dict2))