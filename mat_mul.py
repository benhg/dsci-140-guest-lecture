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
    ## Implement our code here

def matmul(A, B):
    """
    Multiply matrix A and B

    A,B: (List[List[int]])

    return the result matrix
    """
    # Number of columns of A must be the same as rows of B
    num_cols_a = len(A[0])
    num_rows_a = len(A)
    num_rows_b = len(B)
    num_cols_b = len(B[0])

    if (num_cols_a != num_rows_b):
        print("Illegal Matrix")
        return False

    output = []

    # Create the empty matrix
    for i in range(num_rows_a):
        output.append([0] * num_cols_b)

    ## Put our code here
 
    return output


if __name__ == '__main__':

    time_s = time.time()
    print(matmul(A1, B1))
    time_e = time.time()
    print(f"Total time: {time_e - time_s} seconds")
