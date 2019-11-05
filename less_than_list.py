a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
limit = int(input('See numbers less than: '))

b = [item for item in a if item < limit]

print(b)
