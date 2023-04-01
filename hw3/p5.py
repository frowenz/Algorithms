import pandas as pd
import numpy as np
import random

n = 8
matrix = [[random.choice([0, 1]) for x in range(n)] for y in range(n)]

def _sum(arr):
    sum = 0
    for i in arr:
        if (i != 'X'):
            sum = sum + i
    return((n-1)-sum)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if (j<i):
            matrix[i][j] = int(not matrix[j][i])
        if (j==i):
            matrix[i][j] = "X"

def print_matrix(matrix):
    max_len = 0
    for row in matrix:
        print(" ".join("{:<{}}".format(element, max_len) for element in row), end=" ")
        print("|", _sum(row))


print("\n")
print_matrix(matrix)
print("\n")