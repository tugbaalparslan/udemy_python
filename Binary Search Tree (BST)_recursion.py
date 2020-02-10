class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def print_in_order(root):  # DEPTH FIRST SEARCH

    if root:
        print_in_order(root.left)  # First travers the left nodes
        print(root.val, end=" ")  # Print the data of the node
        print_in_order(root.right)  # now recur on right child


def print_pre_order(root):  # DEPTH FIRST SEARCH

    if root:
        print(root.val, end=" ")
        print_pre_order(root.left)
        print_pre_order(root.right)


def print_post_order(root):  # DEPTH FIRST SEARCH

    if root:
        print_post_order(root.left)
        print_post_order(root.right)
        print(root.val, end=" ")
    else:
        return

#  Given a binary tree, return the in-order traversal of its nodes' values in a list.
def inorder_traversal_returns_list(root):
    list = []
    getting_the_inorder_list(root, list)
    return list

def getting_the_inorder_list(root, list):
    if root:
        getting_the_inorder_list(root.left, list)
        list.append(root.val)
        getting_the_inorder_list(root.right, list)






""" Compute the height of a tree - the number of nodes 
    along the longest path from the root node down to 
    the farthest leaf node 
"""

# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).


def is_symmetric(root):
    return is_mirror(root, root)


def is_mirror(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    return t1.val == t2.val and is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)


# Returns the height of a tree
def height(root):
    if root is None:
        return 0
    else:
        l_height = height(root.left)
        r_height = height(root.right)

        return 1 + max(l_height, r_height)


# Returns the number of nodes of a tree
def count_nodes(root):
    if root:
        if root.right and root.left:
            return 1 + count_nodes(root.left) + count_nodes(root.right)
        elif root.right:
            return 1 + count_nodes(root.right)
        elif root.left:
            return 1 + count_nodes(root.left)
        else:
            return 1
    else:
        return 0


# Print nodes at a given level
def print_given_level(root, level):
    if root is None:
        return
    if level == 1:
        print(root.val, end=" ")
    elif level > 1:
        print_given_level(root.left, level-1)
        print_given_level(root.right, level-1)


# This is a Breadth-First Search Algorithm
def print_level_order(root):
    h = height(root)
    for i in range(1, h+1):
        print_given_level(root, i)

# Root 1 (this is a binary tree, not a binary search tree)
#        1
#     /     \
#    2       3
#   / \     / \
#  4   5   6   7
#       \
#        8

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.left = Node(6)
root1.right.right = Node(7)
root1.left.right.right = Node(8)


# print("Printing in-order:")
# print_in_order(root1)
# print("\nPrinting pre-order:")
# print_pre_order(root1)
# print("\nPrinting post-order:")
# print_post_order(root1)
#
# print("\nINORDER TRAVERSAL LIST", inorder_traversal_returns_list(root1)) # WILL DO LATER

print("printing the height of the tree:", height(root1))
print("Printing the number of nodes of the tree:", count_nodes(root1))
print("printing the values of the tree using breadth first search - level order traversal: ")
print_level_order(root1)


# Given two binary trees, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
def is_same_tree(p, q) -> bool:
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False
    return is_same_tree(p.right, q.right) and is_same_tree(p.left, q.left)


# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
def is_mirror(t1, t2):
    if t1 is None and t2 is None:
        return True
    if t1 is None or t2 is None:
        return False
    return t1.val == t2.val and is_mirror(t1.left, t2.right) and is_mirror(t1.right, t2.left)


def is_symmetric(root):
    return is_mirror(root, root)

# Invert a binary tree.
#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9

#     4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1


def invert_tree(root):

    if root:
        root.right, root.left = root.left, root.right
        invert_tree(root.left)
        invert_tree(root.right)

# The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node.
# Otherwise, the NOT null node will be used as the node of new tree.
# Input:
# 	Tree 1                     Tree 2
#           1                         2
#          / \                       / \
#         3   2                     1   3
#        /                           \   \
#       5                             4   7

# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \
# 	 5   4   7
def merge_the_nodes(t1, t2):
    if t1 and t2:
        t1.val = t1.val + t2.val
        t1.left = merge_the_nodes(t1.left, t2.left)
        t1.right = merge_the_nodes(t1.right, t2.right)
    elif not t1:
        t1 = t2
    return t1




root2 = Node(4)
root2.left = Node(2)
root2.left.left = Node(1)
root2.left.right = Node(3)
root2.right = Node(7)
root2.right.left = Node(6)
root2.right.right = Node(9)

print("\nprinting root2:")
print_level_order(root2)
print("\nprinting root2 after inverting:")
invert_tree(root2)
print_level_order(root2)


# Binary Search Tree:
#      4
#    /   \
#   2     7
#  / \
# 1   3

root3 = Node(4)
root3.left = Node(2)
root3.right = Node(7)
root3.left.left = Node(1)
root3.left.right = Node(3)


# Given the root node of a binary search tree (BST) and a value.
# You need to find the node in the BST that the node's value equals the given value.
# Return the subtree rooted with that node. If such node doesn't exist, you should return NULL.

print("\nroot3 is:")
print_level_order(root3)

def search_binary_search_tree(root, val):
    if root:
        if root.val == val:
            return root
        elif val > root.val:
            return search_binary_search_tree(root.right, val)
        else:
            return search_binary_search_tree(root.left, val)


root_result = search_binary_search_tree(root3, 2)
print("\nBinary search Tree result is:")
print_level_order(root_result)


# Merged tree:
# 	     10
# 	    /  \
# 	  5     15
# 	 / \      \
# 	3   7      18
# Given the root node of a binary search tree,return the sum of values of all nodes with value between L and R (inclusive)
# The binary search tree is guaranteed to have unique values.

tree4 = Node(10)
tree4.left = Node(5)
tree4.right = Node(15)
tree4.left.left = Node(3)
tree4.left.right = Node(7)
tree4.right.right = Node(18)


def range_sum_BST(root, L, R):
    if root:
        if L <= root.val <= R:
            return root.val + range_sum_BST(root.left, L, R) + range_sum_BST(root.right, L, R)
        elif root.val < L:
            return range_sum_BST(root.right, L, R)
        elif root.val > R:
            return range_sum_BST(root.left, L, R)
    else:
        return 0

print("Range sum is:", range_sum_BST(tree4, 5, 10))


# Implement pow(x, n), which calculates x raised to the power n (xn).
def my_pow(x, n):
    # if n == 0: # ERROR: Recursive function throws error of max system stack is reached!
    #     return 1
    # elif n > 0:
    #     return x*my_pow(x, n-1)
    # elif n < 0:
    #     return 1/x*(my_pow(x, n+1))
    result = 1
    if n > 0:
        while n > 0:
            result *= x
            n -= 1
    else:
        while n < 0:
            result *= 1/x
            n += 1

    return result




print("Power :", my_pow(2.1, 3))


