import random

list = []

for i in range(15):
    random_number = random.randint(1, 100)
    list.append(random_number)

print("\n")
print("print list before sorting")
print(list)

list.sort(reverse=True)

print("\n")
print("print list after sorting")
print(list)

print("\n")
print("print list before slicing")
print(list)

print("\n")
print("print list after slicing")
print(list[1::2])

