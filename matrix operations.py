def print_matrix(arr):
    x = len(arr[0])
    y = len(arr)

    print(arr)

    for j in range(y):
        for i in range(x):
            print(A[j][i])

    visited = [[False for i in range(x)] for j in range(y)]
    print(visited)


A = [[1, 4, 5, 12],
    [-5, 8, 9, 0],
    [-6, 7, 11, 19]]

print_matrix(A)

a = 0 or 5
print(a)

my_list = [1,2,3,1,3,4,5]
my_dic = {}
del_index = []

st = 0
for x in my_list:
    if x in my_dic.keys():
        del_index.append(st)
    else:
        my_dic[x] = 1

    st += 1

for i in range(-1, -len(del_index) -1, -1):
    del my_list[del_index[i]]

print(my_list)


arr = [17,18,5,4,6,1]

max_num = arr[-1] - 1
for i in range(-1, -len(arr) - 1, -1):
    print(arr[i])
    cur = arr[i]
    arr[i] = max_num
    if cur > max_num:
        max_num = cur

arr[-1] = -1
print(arr)




