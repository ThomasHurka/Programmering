

unsortednum = [4, 3, 6, 623, 53, 7, 1414, 8765323456]
even = list(filter(lambda x: (x % 2 == 0), unsortednum))
odd = list(filter(lambda x: (x % 2 != 0), unsortednum))
print(even)
print(odd)
