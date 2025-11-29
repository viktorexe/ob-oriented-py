# A dictionary stores data in key value pairs

student = {
    'name' : 'Vansh',
    'age' : 12,
    'City' : 'Jaipur'
}

print(student['age'])

# Adding new 
student["marks"] = 90
print(student['marks'])

# Removes key 
student.pop('age')

# Print all keys
print(student.keys())

# Print the values
print(student.values())

# Print value pairs
print(student.items())