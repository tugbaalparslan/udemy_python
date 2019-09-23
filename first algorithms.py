num_array = [15,8,98,23,7,1,67,90,56,3,88,101]

# print(num_array)


# we are gonna find the min item of the list

import sys
min = sys.maxsize

for x in num_array:
    if x < min:
        min = x


print(f"Min num int he list is: {min}")


# we are gonna find the second min number in a given list


min1 = sys.maxsize -1
min2 = sys.maxsize


for x in num_array:
    if x < min1:
        min2 = min1
        min1 = x
    elif x < min2:
        min2 = x

print(f"Min1 = {min1}, Min2 = {min2}")

