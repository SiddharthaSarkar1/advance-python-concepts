numbers = [12, 14, 23, 18, 56, 34, 42, 98]

def square(num: int) -> int:
    return num*num

new_list = []

for number in numbers:
    new_list.append(square(number))

print(new_list)

#============================================
# Using MAP function

new_list2 = map(square, numbers)

print(new_list2) # its a map object

print(list(new_list2)) # Need to typecast it to a list