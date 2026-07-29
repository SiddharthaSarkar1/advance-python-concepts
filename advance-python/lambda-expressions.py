mysquare = lambda x: x ** 2

mysum = lambda x,y: x+y

my_sum = lambda *args: sum(args) 

print(mysquare(5))
print(mysum(2, 6))

print(my_sum(1, 2, 3))
print(my_sum(1, 2, 3, 4, 5))

print((lambda x,y: x*y)(5, 7))

#===============================================================================

numbers = [8, 66, 34, 5, 17, 13, 25, 43, 19, 109, 88, 76, 52, 36, 112]

even_number_list = list(filter(lambda x: x%2 == 0, numbers))

squared_num_list = list(map(lambda x: x**2, even_number_list))

print(even_number_list)

print(squared_num_list)

#==================================================================

def myfunc(num):
    return lambda x: x*num

ten_multiplier = myfunc(10)
print(ten_multiplier(5))

two_multiplier = myfunc(2)
print(two_multiplier(5))