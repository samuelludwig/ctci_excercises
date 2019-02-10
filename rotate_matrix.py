"""
    Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes, write a method 
    to rotate the image by 90 degrees. Can you do it in place?
    (I am assuming the matrix is taken in as a list)
""" 
import math
# [0000, 1111, 2222]

# [3333, 4444, 5555]

# [6666, 7777, 8888]

# #       |        #
# #       V        #

# [6666, 3333, 0000]

# [7777, 4444, 1111]

# [8888, 5555, 2222]


# [0, 1, 2, 3, 4, 5, 6, 7, 8] -> 
# [6, 3, 0, 7, 4, 1, 8, 5, 2]

# [01, 02, 03, 04]
# [05, 06, 07, 08]
# [09, 10, 11, 12]
# [13, 14, 15, 16]
#         |
#         V
# [13, 09, 05, 01]
# [14, 10, 06, 02]
# [15, 11, 07, 03]
# [16, 12, 08, 04]

# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16] -> 
# [13, 9, 5, 1, 14, 10, 6, 2, 15, 11, 7, 3, 16, 12, 8, 4]

class matrix():
    def __init__(self):
        pass

def left(num):
    return (num-1)

def right(num):
    return (num+1)

def up(num, dim):
    return (num-dim)

def down(num, dim):
    return (num+dim)

def rotate(this_matrix):
    matrix_dim = math.sqrt(this_matrix.__len__())


""" TEST METHODS """

def is_rotated_odd_dim():
    if (rotate([0, 1, 2, 3, 4, 5, 6, 7, 8]) == [6, 3, 0, 7, 4, 1, 8, 5, 2]):
        return 1
    else:
        return 0

def is_rotated_even_dim():
    if (rotate([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) 
            == [13, 9, 5, 1, 14, 10, 6, 2, 15, 11, 7, 3, 16, 12, 8, 4]):
        return 1
    else:
        return 0

if __name__ == "__main__":
    print(is_rotated_odd_dim())
    print(is_rotated_even_dim())