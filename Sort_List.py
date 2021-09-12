number_list = [12,5,65,45,15,7,12,97,54,236,21,14,56]
for j in range(2):
    for i in range(len(number_list)-1):
        if number_list[i] > number_list[i+1]:
            number_list[i],number_list[i+1] = number_list[i+1],number_list[i]
print(number_list)
print(number_list[-2],number_list[-1])

