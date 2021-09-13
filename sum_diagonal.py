from random import choice
number = [0,1,2,3,4,5,6,7,8,9]
def get_matrix_number(n):
    random_matrix = [[choice(number) for e in range(n)] for e in range(n)]
    return  random_matrix

def sum_diagonal(matrix,n):
    sum = 0
    for i in range(n):
        sum += matrix[i][i]
    return sum
matrix =get_matrix_number(3)
sum = sum_diagonal(matrix,3)
print(matrix)
print(sum)
