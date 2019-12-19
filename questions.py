import sys


def first_two_sum(my_list, sumsum):  # returns the first two_sum index pair

    for counter1 in range(0, len(my_list)):
        for counter2 in range(counter1 + 1, len(my_list)):
            if my_list[counter1] + my_list[counter2] == sumsum:
                return counter1, counter2
        print(counter2)


def tuple_list_two_sum(mylist, sumsum):  # returns all index pair of two sums as tuple list
    tuple_two_sum_indexes = []
    for counter1 in range(0, len(my_list)):
        for counter2 in range(counter1 + 1, len(my_list)):
            if my_list[counter1] + my_list[counter2] == sumsum:
                tuple_two_sum_indexes.append((counter1, counter2))

    return tuple_two_sum_indexes


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


def replace_with_the_greatest_next(arr):

    for i in range(len(arr)-1):
        max_int = -sys.maxsize
        for ii in range(i+1, len(arr)):
            if arr[ii] > max_int:
                max_int = arr[ii]
        arr[i] = max_int

    print(arr)


def reverse_the_list(my_arr):
    end_pos = len(my_arr) - 1
    beg_pos = 0
    loop_x = int(len(my_arr)/2)

    while loop_x > 0:
        temp_x = my_arr[end_pos]
        my_arr[end_pos] = my_arr[beg_pos]
        my_arr[beg_pos] = temp_x
        end_pos -= 1
        beg_pos += 1
        loop_x -= 1

    print("reversed list is:", my_arr)



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


def count_num_of_occurrences(my_arr):  # Counts each number's occurrences in a given list
    my_dict = {}

    for x in my_arr:
        if str(x) in my_dict.keys():
            my_dict[str(x)] += 1
        else:
            my_dict[str(x)] = 1

    print("Counted nums:", my_dict)


def find_min_and_max_of_list(my_arr):  # Finds min and max items of a given list using brute force
    min_num = sys.maxsize
    max_num = -sys.maxsize

    for x in my_arr:
        if x < min_num:
            min_num = x
        if x > max_num:
            max_num = x
    print(f"min: {min_num}, max:{max_num}")


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


def find_min1_min2(my_arr):  # Finds the first and second min values in a given list
    min1 = min2 = sys.maxsize

    for cur_val in my_arr:
        if cur_val < min1:
            min2 = min1
            min1 = cur_val
        elif cur_val < min2:
            min2 = cur_val
    print("Min1: {} and Min2: {}".format(min1, min2))


def find_the_num_by_slicing_the_sorted_list_half(my_arr, num):
    low = 0
    high = len(my_arr)-1

    while low <= high:
        mid = (low + high) // 2

        if num == my_arr[mid]:
            return mid
        elif num > my_arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# my_arr is a sorted list
def find_the_first_element_larger_than_x(my_arr, num):
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




my_list = [0, 2, 0, -8, 1, 3, 0, 0, 5, 4, 19]
reverse_the_list(my_list)  # after this function, changes made in the function affects my_list in the main body


my_list = [0, 2, 5, 8, -1, 2]
shift_arr_n_times(my_list, 2)

print("My list after shifting in main body: {}".format(my_list))
print(first_two_sum(my_list, 7))
print(tuple_list_two_sum(my_list, 7))
print("my list: {} smart two sum tuple list".format(my_list), smart_two_sum(my_list, 7))

remove_num_occurrences_from_list(my_list, 0)

replace_with_the_greatest_next(my_list)

my_list = [0, 2, 0, 8, 1, -3, 0, 0, 5, 4, -11]

count_num_of_occurrences(my_list)

find_min_and_max_of_list(my_list)

find_min_and_max_of_list_least_comparing(my_list)

find_min1_min2(my_list)

my_list = [1, 2, 5, 6, 9, 12]
print("sliced : ", find_the_num_by_slicing_the_sorted_list_half(my_list,1))


my_list = [0, 2, 0, -8, 1, 3, 0, 0, 5, 4, 19, 12]
my_list.sort()
print(find_the_first_element_larger_than_x(my_list, 11))

my_list = [-1,0,3,5,9,12]
print("result of recursive search is:", binary_search_recursive(my_list, 0, len(my_list) - 1, 9))