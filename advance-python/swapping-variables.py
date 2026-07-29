a = 10
b = 20

print(f"Before Swapping: a = {a}, b = {b}")

a = a + b # a=30 b=20
b = a - b # a=30 b=(30-20)=10
a = a - b # a=(30-10)=20 b=10

print(f"After Swapping: a = {a}, b = {b}")