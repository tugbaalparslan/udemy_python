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


# removes all occurrences of a given num in a given list
# without using the remove function or creating a new list


def remove_num_occurrences_from_list(arr, num_to_remove):
    loc_index = 0
    for cur_item in arr:
        if cur_item != num_to_remove:
            arr[loc_index] = cur_item
            loc_index += 1

    del arr[loc_index:]
    print(arr)


def replace_with_the_greatest_next(arr):
    import sys

    for i in range(len(arr)-1):
        max_int = -sys.maxsize
        for ii in range(i+1, len(arr)):
            if arr[ii] > max_int:
                max_int = arr[ii]
        arr[i] = max_int

    print(arr)


def remove_all_zeros_from_list(arr):
    fill_pos = 0
    for cur_val in arr:
        if cur_val != 0:
            arr[fill_pos] = cur_val
            fill_pos += 1

    for i in range(fill_pos, len(arr)):
        arr[i] = 0

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

    print("reverse list:", my_arr)


my_list = [0, 2, 0, 8, 1, 3, 0, 0, 5, 4, 9]
reverse_the_list(my_list)



my_list = [1, -1, 3, 5, 8, 11, -1, 8, -2, 9, 4, 1, 1, 1, 8]
print(first_two_sum(my_list, 7))
print(tuple_list_two_sum(my_list, 7))
print(smart_two_sum(my_list, 7))

remove_num_occurrences_from_list(my_list, 1)

replace_with_the_greatest_next(my_list)
my_list = [0, 2, 0, 8, 1, 3, 0, 0, 5, 4]
remove_all_zeros_from_list(my_list)


