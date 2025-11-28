# Logical operators combine multiple True False conditions

x = 10
print(x > 5 and x < 20)    # True
print(x > 5 and x < 8)     # False

# We can reverse the results by using a not
y = 10
print(not(y == 10 and y < 15))