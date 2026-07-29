mynames = ["soumya", "john", "bunty", "mampi", "dolly", "boni", "bukku", "joba", "darik"]

print(list(enumerate(mynames)))

for index, name in enumerate(mynames):
    print(f"{index}: {name}")

# Output

# [(0, 'soumya'), (1, 'john'), (2, 'bunty'), (3, 'mampi'), (4, 'dolly'), (5, 'boni'), (6, 'bukku'), (7, 'joba'), (8, 'darik')]

# 0: soumya
# 1: john
# 2: bunty
# 3: mampi
# 4: dolly
# 5: boni
# 6: bukku
# 7: joba
# 8: darik