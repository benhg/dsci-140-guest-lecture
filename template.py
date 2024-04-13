"""
Matrix Multiplication

Multiply two matrices of arbitrary size 
by each other to find a new matrix
"""

import time

A1 = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
     ]

B1 = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
     ] 

def dot_product(a_vec, b_vec):
    """
    Compute the dot product of two vectors
    """
    pass


def matmul(A, B):
    """
    Our code will go here
    """
    # Number of columns of A must be the same as rows of B
    width = len(A[0])
    height = len(B)

    if (width != height):
        print("Illegal Matrix")
        return False

    output = []

    # Create the empty matrix
    for i in range(height):
        output.append([0] * width)

    ## Put our code here
    ##
 

    return output


if __name__ == '__main__':

    time_s = time.time()
    print(matmul(A1, B1))
    time_e = time.time()
    print(f"Total time: {time_e - time_s} seconds")