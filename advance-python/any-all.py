# any() -> returns true when one of its collection returns True
# all() -> returnd true if all of its collection returns True


x = [False, False, False, True, False, False, False]
print(any(x))
print(all(x))

y = [True, True, True]
print(any(y))
print(all(y))

z = [False, False, False]
print(any(z))
print(all(z))

#===================================================

numbers = [11, 12, 22, 8, 72, 55, 44, 31, 17]

even = lambda x: x%2 == 0 

results = [even(number) for number in numbers]

if any(results):
    print("There is at least one even number")
else:
    print("No number is even")

if all(results):
    print("All the numbers are even")