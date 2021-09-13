lst1 = [2,4,5,6,8]

def get_prime(x):
    count = 0
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1
    if count == 2:
        return True
    return False

new_list1 =[x for x in lst1 if get_prime(x) ==True]

print(new_list1)
