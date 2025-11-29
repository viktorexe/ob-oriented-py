# Shortcut to make list, set, dict using loop 
# [x for x in iterable]

result = []

for x in range(5):
    result.append(x*x)
    
print(result)

d = {x: x*x for x in range(5)}
print(d)