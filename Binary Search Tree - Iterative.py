# A node structure
class Node:

    # A utility function to create a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None

# ITERATIVE Python program for level order traversal of Binary Tree
# returns each nodes values in a 1 dimensional list using level ordering ( breadth first search)
# returns [1, 2, 3, 4, 5]


def level_order_list(root):
    queue = []
    val_list = []

    if root:
        queue.append(root)
    else:
        return None

    while len(queue):
        cur_node = queue.pop(0)
        val_list.append(cur_node.data)

        if cur_node.left:
            queue.append(cur_node.left)
        if cur_node.right:
            queue.append(cur_node.right)

    return val_list


# returns each level's node values in a nested list using level ordering ( breadth first search):
# returns [[1], [2, 3], [4, 5]]


def level_order_nested_list(root):
    queue = []
    whole_list = []
    inner_list = []

    if root:
        queue.append((1, root))  # store each level in tuple (node, level)
        cur_level = 1
    else:
        return None

    while len(queue):
        level, cur_node = queue.pop(0)

        if level == cur_level:  # still looping through the same level
            inner_list.append(cur_node.data)
        else:                   # level is changed, time to append the previous inner list to whole list
            whole_list.append(inner_list)
            cur_level = level
            inner_list = [cur_node.data]

        if cur_node.left:
            queue.append((level + 1, cur_node.left))
        if cur_node.right:
            queue.append((level + 1, cur_node.right))

    whole_list.append(inner_list)  # append the last value of inner list

    return whole_list

# returns each level's node values in a nested list using level ordering ( breadth first search):
# In this solution, I first stored the nested lists in a dictionary {level: [inner_list]}
# returns [[1], [2, 3], [4, 5]]


# def level_order_nested_list(root):
#     queue = []
#     val_list = {}  # each nested list is stored in a dic: {1: [1], 2: [2, 3], 3: [4, 5]}
#
#     if root:
#         queue.append((1, root))
#     else:
#         return None
#
#     while len(queue):
#         level, cur_node = queue.pop(0)
#
#         if level not in val_list.keys():
#             val_list[level] = [cur_node.data]
#         else:
#             for key, val in val_list.items():
#                 if key == level:
#                     val.append(cur_node.data)
#
#         if cur_node.left:
#             queue.append((level + 1, cur_node.left))
#         if cur_node.right:
#             queue.append((level + 1, cur_node.right))
#
#     nested_list = []
#     for key, val in val_list.items():  # time to convert dic values into a nested list
#         nested_list.append(val)
#
#     return nested_list


def zigzag_traversal_nested_listed(root):
    stack1 = []
    stack2 = []
    whole_list = []
    inner_list = []

    if root:
        stack1.append(root)

    while stack1 or stack2:
        while stack1:
            cur_node = stack1.pop()
            inner_list.append(cur_node.data)
            if cur_node.left:
                stack2.append(cur_node.left)
            if cur_node.right:
                stack2.append(cur_node.right)

        if inner_list:
            whole_list.append(inner_list)
        inner_list = []
        while stack2:
            cur_node = stack2.pop()
            inner_list.append(cur_node.data)

            if cur_node.right:
                stack1.append(cur_node.right)
            if cur_node.left:
                stack1.append(cur_node.left)

        if inner_list:
            whole_list.append(inner_list)
        inner_list = []

    return whole_list


def flatten_binary_tree_to_right_in_level_order(root):

    nodes_queue = []
    new_nodes = Node(1)
    new_head = new_nodes

    if root:
        nodes_queue.append(root)

    while len(nodes_queue):
        popped_node = nodes_queue.pop(0)
        new_nodes.right = popped_node
        new_nodes.left = None

        if popped_node.left:
            nodes_queue.append(popped_node.left)
        if popped_node.right:
            nodes_queue.append(popped_node.right)

        new_nodes = new_nodes.right

    return new_head.right


# find if a given number is in a binary search tree or not. True if found, false if not.
def search_binary_tree_iteratively(root, val):
    cur_node = root

    while True:
        if not cur_node:
            return False
        elif cur_node.data == val:
            return True
        elif val > cur_node.data:
            cur_node = cur_node.right
        elif val < cur_node.data:
            cur_node = cur_node.left


# Iterative function for post-order tree traversal # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
def post_order_iterative_printing(root):
    pass
# This is a HARD leetcode question -- you can solve this by using 2 stacks: https://youtu.be/qT65HltK2uE


# Iterative function for pre-order tree traversal
def pre_order_iterative_printing(root):

    stack_nodes = []

    if root:
        stack_nodes.append(root)
    while stack_nodes:
        popped_node = stack_nodes.pop(-1)
        print(popped_node.data)

        if popped_node.right:
            stack_nodes.append(popped_node.right)
        if popped_node.left:
            stack_nodes.append(popped_node.left)


# Iterative function for in-order tree traversal
# This is good for converting a binary search tree to a binary search list
def in_order_iterative_printing(root):
    # Set current to root of binary tree
    current = root
    stack = []  # initialize stack

    while True:
        # Reach the left most Node of the current Node
        if current is not None:
            # Place pointer to a tree node on the stack
            # before traversing the node's left subtree
            stack.append(current)
            current = current.left
        # BackTrack from the empty subtree and visit the Node
        # at the top of the stack; however, if the stack is
        # empty you are done
        elif stack:
            current = stack.pop()
            print(current.data, end=" ")  # Python 3 printing
            # We have visited the node and its left
            # subtree. Now, it's right subtree's turn
            current = current.right
        else:
            break


# Root 1 (this is a binary tree, not a binary search tree)
#            1
#       /        \
#      2          3
#    /  \         / \
#   4     5      6   7
#  / \   / \     /\
# 8   9 10 11  12 13

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.left = Node(6)
root1.right.right = Node(7)
# root1.left.left.left = Node(8)
# root1.left.left.right = Node(9)
# root1.left.right.left = Node(10)
# root1.left.right.right = Node(11)
# root1.right.left.left = Node(12)
# root1.right.left.right = Node(13)

# print("Level order traversal of binary tree is : {}".format(level_order_list(root1)))
# print("Level order traversal of binary tree is : {}".format(level_order_nested_list(root1)))
# print("Zigzag traversal of binary tree is : {}".format(zigzag_traversal_nested_listed(root1)))

# root_flattened = flatten_binary_tree_to_right(root1)
# print("Level order traversal of binary tree is : {}".format(level_order_list(root_flattened)))

pre_order_iterative_printing(root1)
print("Post order traversal of the binary tree is:", post_order_iterative_printing(root1))

print(search_binary_tree_iteratively(root1, 6))

x = 0011

print("---", ~x)








