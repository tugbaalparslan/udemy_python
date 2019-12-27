import sys


def first_two_sum(my_list, sumsum):  # returns the first two_sum index pair

    for counter1 in range(0, len(my_list)):
        for counter2 in range(counter1 + 1, len(my_list)):
            if my_list[counter1] + my_list[counter2] == sumsum:
                return counter1, counter2


my_list = [-1, 2, 0, -8, -4, -9, 1, 3, 0, 0, 5, 4, 19, 12, 15, 18, 19]
print("first two sum index pair is:", first_two_sum(my_list, 7))


def tuple_list_two_sum(mylist, sumsum):  # returns all index pair of two sums as tuple list
    tuple_two_sum_indexes = []
    for counter1 in range(0, len(my_list)):
        for counter2 in range(counter1 + 1, len(my_list)):
            if my_list[counter1] + my_list[counter2] == sumsum:
                tuple_two_sum_indexes.append((counter1, counter2))

    return tuple_two_sum_indexes


print("all index pairs of two sums is:", tuple_list_two_sum(my_list, 7))


def smart_two_sum(mylist, sumsum):  # returns all index pair of two sums as tuple list
    temp_dict = {}
    two_sum_tuple_list = []

    for count in range(len(my_list)):
        for keys in temp_dict:
            if temp_dict[keys] == my_list[count]:
                two_sum_tuple_list.append((keys, count))

        required_num = sumsum - my_list[count]
        temp_dict[count] = required_num
    return two_sum_tuple_list


print("smart two sum tuple list:", smart_two_sum(my_list, 7))


# removes all occurrences of a given number in a given list
# without using the remove function or creating a new list
def remove_num_occurrences_from_list(arr, num_to_remove):
    loc_index = 0
    for cur_item in arr:
        if cur_item != num_to_remove:
            arr[loc_index] = cur_item
            loc_index += 1

    del arr[loc_index:]
    print("In function:", sys._getframe(  ).f_code.co_name,":", arr)


my_list = [0, 1, 2, 3, 0, 4, 0]
remove_num_occurrences_from_list(my_list, 0)


def replace_with_the_greatest_next(arr):

    for i in range(len(arr)-1):
        max_int = -sys.maxsize
        for ii in range(i+1, len(arr)):
            if arr[ii] > max_int:
                max_int = arr[ii]
        arr[i] = max_int

    print(arr)


my_list = [0, 1, 8, 3, 4]
replace_with_the_greatest_next(my_list)


def reverse_the_list(my_arr):
    end_pos = len(my_arr) - 1
    beg_pos = 0

    while beg_pos < end_pos:
        my_arr[end_pos], my_arr[beg_pos] = my_arr[beg_pos], my_arr[end_pos]
        end_pos -= 1
        beg_pos += 1

    print("reversed list is:", my_arr)


my_list = [0, 1, 2, 3, 4]
reverse_the_list(my_list)  # after this function, changes made in the function affects my_list in the main body


def shift_arr_n_times(my_list, n):     # tis code needs optimization, time out for huge arrays

    if n > len(my_list):
        n = n % len(my_list)

    while n > 0:
        last = my_list[len(my_list)-1]

        for i in range(len(my_list)-2, -1, -1):
            my_list[i+1] = my_list[i]
        my_list[0] = last
        n -= 1

    print('shifted list is:', my_list)


my_list = [0, 2, 5, 8, -1, 2]
shift_arr_n_times(my_list, 2)


def count_num_of_occurrences(my_arr):  # Counts each number's occurrences in a given list
    my_dict = {}

    for x in my_arr:
        if x in my_dict.keys():
            my_dict[x] += 1
        else:
            my_dict[x] = 1

    print("Counted nums:", my_dict)


my_list = [0, 2, 0, 8, 1, -3, 0, 0, 5, 4, -11]
count_num_of_occurrences(my_list)


def find_min_and_max_of_list(my_arr):  # Finds min and max items of a given list using brute force
    min_num = sys.maxsize
    max_num = -sys.maxsize

    for x in my_arr:
        if x < min_num:
            min_num = x
        if x > max_num:
            max_num = x
    print(f"min: {min_num}, max:{max_num}")


my_list = [-1, 2, 0, -8, -9, 1, 3, 0, 0, 5, 4, 19, 12, 15, 18, 19]
find_min_and_max_of_list(my_list)


def find_min_and_max_of_list_least_comparing(my_arr):   # Finds min and max items of a given list using least comparing

    if len(my_arr) % 2 == 1:
        start_index = 1
        max_val = min_val = my_arr[0]
    else:
        start_index = 0
        max_val = -sys.maxsize
        min_val = sys.maxsize

    for i in range(start_index, int(len(my_arr)), 2):
        if my_arr[i] > my_arr[i+1]:
            local_max = my_arr[i]
            local_min = my_arr[i+1]
        elif my_arr[i] < my_arr[i+1]:
            local_min = my_arr[i]
            local_max = my_arr[i + 1]

        if max_val < local_max:
            max_val = local_max
        if min_val > local_min:
            min_val = local_min

    print("max val: {} min val: {}".format(max_val, min_val))


my_list = [-1, 2, 0, -8, -9, 1, 3, 0, 0, 5, 4, 19, 12, 15, 18, 19]
find_min_and_max_of_list_least_comparing(my_list)


def find_min1_min2(my_arr):  # Finds the first and second min values in a given list
    min1 = min2 = sys.maxsize

    for cur_val in my_arr:
        if cur_val < min1:
            min2 = min1
            min1 = cur_val
        elif cur_val < min2:
            min2 = cur_val
    print("Min1: {} and Min2: {}".format(min1, min2))


my_list = [-1, 2, 0, -8, -9, 1, 3, 0, 0, 5, 4, 19, 12, 15, 18, 19]
find_min1_min2(my_list)


# my_arr is a sorted list
def find_the_next_greater_element_in_a_sorted_list(my_arr, num):
    low = 0
    high = len(my_arr) - 1
    first_max = sys.maxsize

    while low <= high:
        mid = (low + high) // 2

        if my_arr[mid] <= num:
            low = mid + 1
        elif my_arr[mid] > num:
            first_max = my_arr[mid]
            high = mid - 1

    if first_max != sys.maxsize:
        return first_max
    else:
        return False


my_list = [-1, 2, 0, -8, -9, 1, 3, 0, 0, 5, 4, 19, 12, 15, 18, 19]
my_list.sort()
print("next greater occurrence", find_the_next_greater_element_in_a_sorted_list(my_list, -3))


# my_arr is a sorted list
def find_the_next_smaller_element_in_a_sorted_list(my_arr, num):
    low = 0
    high = len(my_arr) - 1
    first_min = sys.maxsize

    while low <= high:
        mid = (low + high) // 2

        if my_arr[mid] < num:
            first_min = my_arr[mid]
            low = mid + 1
        elif my_arr[mid] >= num:
            high = mid - 1

    if first_min != sys.maxsize:
        return first_min
    else:
        return False


my_list = [-1, 2, 0, -8, -4, -9, 1, 3, 0, 0, 5, 4, 19, 12, 15, 18, 19]
my_list.sort()
print("next smaller occurrence", find_the_next_smaller_element_in_a_sorted_list(my_list, -3))


# recursive form of binary search
def binary_search_recursive(arr, st_in, end_i, searched_num):

    if st_in <= end_i:

        mid = (st_in + end_i) // 2

        if arr[mid] == searched_num:
            return mid
        elif arr[mid] < searched_num:
            st_in = mid + 1
            return binary_search_recursive(arr, st_in, end_i, searched_num)
        elif arr[mid] > searched_num:
            end_i = mid - 1
            return binary_search_recursive(arr, st_in, end_i, searched_num)
    else:
        return -1


my_list = [-1, 0, 3, 5, 9, 12]
print("result of recursive search is:", binary_search_recursive(my_list, 0, len(my_list) - 1, 9))



def recursive_factorial(n):
    if n == 1:
        return 1
    else:
        result = n*recursive_factorial(n-1)
        return result
        # return n*recursive_factorial(n-1)  # we can simply return this instead of 2 lines above


print("Factorial of {} is {}".format(4, recursive_factorial(4)))















