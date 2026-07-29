dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 4, 'c': 7}

dict1.update(dict2)

print(dict1)

#====================================

mydict1 = {'a': 1, 'b': 2}
mydict2 = {'b': 4, 'c': 7}

mydict3 = {**mydict1, **mydict2}
mydict4 = {**mydict2, **mydict1}

print(mydict3)
print(mydict4)

#========================================================

mydict1 = {'a': 1, 'b': 2}
mydict2 = {'b': 4, 'c': 7}

my_new_dict = mydict1 | mydict2

print(my_new_dict)