names = ["Anna", "John", "Bob", "Julee", "David", "Marko", "Tito"]
ages = [12, 16, 22, 18, 26, 32, 36]

for i in range(len(names)):
    print(f"Name: {names[i]}, Age: {ages[i]}")

#====================================================
# Using zip
# zip() -> returns a zip object, which is an iterator of tuples where the first item in each passed iterator is paired together, and then the second item in each passed iterator are paired together etc.

for name, age in zip(names, ages):
    print(f"Name: {name}, Age: {age}")

# print(list(zip(names, ages)))

#==========================================================

sales = [200, 300, 400, 500, 630, 721, 345]
costs = [56, 122, 345, 123, 567, 711, 98]

for sale, cost in zip(sales, costs):
    print(f"Profit: ${sale - cost}")

#================================================

# Unzip using zip() method

zipped = [('Anna', 12), ('John', 16), ('Bob', 22), ('Julee', 18), ('David', 26), ('Marko', 32), ('Tito', 36)]

uz_names, uz_ages = zip(*zipped)

print(uz_names)
print(uz_ages)

#========================================

letters = ['b', 'c', 'd', 'a']
nums = [2, 3, 4, 1]

data = sorted(zip(letters, nums))

print(data)

mydict = dict(zip(letters, nums))

print(mydict)