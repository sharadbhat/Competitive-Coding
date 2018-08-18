# HACKERRANK
# https://www.hackerrank.com/challenges/tree-huffman-decoding/problem

"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root, s):
    pointer = root
    for i in s:
        if i == '0':
            if pointer.left != None:
                pointer = pointer.left
        elif i == '1':
            if pointer.right != None:
                pointer = pointer.right
        if pointer.left == None and pointer.right == None:
            print(pointer.data, end='')
            pointer = root
