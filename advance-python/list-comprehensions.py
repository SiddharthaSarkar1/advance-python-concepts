numbers = [12, 18, 15, 14, 17, 23, 11, 54, 71]

new_list = []

for number in numbers:
    if number%2 == 0:
        new_list.append(number)


print(new_list)

# List Comprehensions
new_list2 = [x for x in numbers if x%2 == 0]

print(new_list2)

#===============================================================

my_list = [1,2,3,4,5,6]

power_of_two = [x ** 2 for x in my_list]

print(power_of_two)