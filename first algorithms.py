import sys


def get_min_from_array(int_array):  # we are gonna find the min item of a given list
    minimum = sys.maxsize

    for x in int_array:
        if x < minimum:
            minimum = x

    print(f"Min number in the list is: {minimum}")


def get_min2_from_array(int_array):  # we are gonna find the second min number in a given list
    min1 = min2 = sys.maxsize

    for x in int_array:
        if x < min1:
            min2 = min1
            min1 = x
        elif x < min2:
            min2 = x

    print(f"Min number in the list is: {min1}, Second min number in the list is: {min2}")


num_array = [15, 8, 98, 23, 7, 1, 67, 90, 56, 3, 88, 101, -3]
get_min_from_array(num_array)
get_min2_from_array(num_array)
