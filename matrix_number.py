from random import choice
number = [0,1,2,3,4,5,6,7,8,9]
def get_matrix_number(m,n):
    random_matrix = [[choice(number) for e in range(n)] for e in range(m)]
    return  random_matrix
m = int(input("Nhập hàng: "))
n = int(input("Nhập cột: "))
matrix = get_matrix_number(m,n)
print(matrix)
