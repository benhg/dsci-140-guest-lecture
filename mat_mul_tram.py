"""
Matrix Multiplication

Multiply two matrices of arbitrary size 
by each other to find a new matrix
"""

import time

from multiprocessing import Pool

import numpy as np

A = [[1, 2, 3] * 200,
     [4, 5, 6] * 200,
     [7, 8, 9] * 200
     ] * 200

B = [[1, 2, 3] * 200,
     [4, 5, 6] * 200,
     [7, 8, 9] * 200
     ] * 200 

def dot_product(a_vec, b_vec):
    """
    Compute the dot product of two vectors
    """
    if len(a_vec) != len(b_vec):
        return False
    output = 0
    for i in range(len(a_vec)):
        output += (a_vec[i] * b_vec[i])
    return output


def matmul_serial(A, B):
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

    for i in range(num_rows_a):
        for j in range(num_cols_b):
            a_vec = A[i]
            b_vec = [B[k][j] for k in range(num_rows_b)]
            dot = dot_product(a_vec, b_vec)
            output[i][j] = dot
 
    return output

def dot_product_helper(A, B, i, j):
    num_rows_b = len(B)
    a_vec = A[i]
    b_vec = [B[k][j] for k in range(num_rows_b)]
    dot = dot_product(a_vec, b_vec)
    return (i, j, dot)

def matmul_parallel(A, B):
    """
    Our code will go here
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
 
    # Get a load of cores to do this work for us
    pool = Pool()

    # Construct inputs to our multiprocessing pool
    inputs = []
    for i in range(num_rows_a):
        for j in range(num_cols_b):
            inputs.append((A, B, i, j))
    
    res = pool.starmap(dot_product_helper, inputs)

    for i, j, dot in res:
        output[i][j] = dot 
    
    return output

def matmul_numpy(A, B):
    """
    Mat Mul using a highly tuned library
    """
    output = np.matmul(A, B)
    return(output)


if __name__ == '__main__':

    time_s = time.time()
    matmul_serial(A, B)
    time_e = time.time()
    print(f"Total time (Serial): {time_e - time_s} seconds")

    time_s = time.time()
    matmul_parallel(A, B)
    time_e = time.time()
    print(f"Total time (Parallel): {time_e - time_s} seconds")


    time_s = time.time()
    matmul_numpy(A, B)
    time_e = time.time()
    print(f"Total time (NumPy Package): {time_e - time_s} seconds")

