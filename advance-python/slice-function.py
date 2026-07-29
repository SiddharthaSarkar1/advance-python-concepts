numbers = [10, 90, 22, 55, 34, 67, 87, 94, 53, 107]

print(numbers[5])
print(numbers[2:-4])

LASTFOUR = slice(-4, None)
FIRSTFOUR = slice(4)

EVERY_OTHER = slice(0, None, 2)
EVERY_THIRD = slice(0, None, 3)


print(numbers[LASTFOUR])

print(numbers[FIRSTFOUR])

print(numbers[EVERY_OTHER])

print(numbers[EVERY_THIRD])


# 67
# [22, 55, 34, 67]
# [87, 94, 53, 107]
# [10, 90, 22, 55]
# [10, 22, 34, 87, 53]
# [10, 55, 87, 107]