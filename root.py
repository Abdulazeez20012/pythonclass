def my_list():
    my_list = [4]
    for x in my_list:
        my_list.append(x**3)  
    return my_list

result = my_list()
print(result)
