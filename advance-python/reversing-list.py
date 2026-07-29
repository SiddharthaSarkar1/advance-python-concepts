# Reversing a list using for loop

values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

rev_list = []

for index in range(len(values)):
    rev_list.append(values[len(values) - index - 1])

print(rev_list)
#========================================================
# Using reverse() method

values2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
values2.reverse()
print(values2)

#========================================================
# Using reversed() method

rev_list3 = []
rev_list3 = reversed(values)
print(list(rev_list3))

#===================================================
# Using slicing

my_values = [10, 20, 30,40, 50]

my_values = my_values[::-1]

print(my_values)