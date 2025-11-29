# Set are unordered no indexing, duplicates removed automatically


my_set = {1, 2, 4, 0, 11, 4}
print(my_set) # Always prints sorted 

# Adding an element, append is not in sets
my_set.add(41)
print(my_set)

# Update
my_set.update([33, 12])
print(my_set)

# Remove
my_set.remove(1)
print(my_set)

# Check for availability
print(2 in my_set) # True if exists else false
