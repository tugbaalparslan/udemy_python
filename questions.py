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


def first_two_sum(my_list, sumsum):  # returns the first two_sum index pair
    list_len = len(my_list)
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


my_list = [1, -1, 3, 5, 8, 11, -1, 8, -2, 9, 4, 1, 1, 1, 8]
print(first_two_sum(my_list, 7))
print(tuple_list_two_sum(my_list, 7))
print(smart_two_sum(my_list, 7))

remove_num_occurrences_from_list(my_list, 1)