# Iterator is something which separates each element of an interable thing using next()

nums = [1, 2, 3, 4, 5, 6]
it = iter(nums)
print(next(it)) # Will print 1
print(next(it)) # Will print 2
print(next(it)) # Will print 3

# This is exactly what for loop does 
