my_list = [1,2,3]
new_list = ((my_list * 2)[1:5] + list((7,8)))*4
print(str((my_list+new_list).count(2)))