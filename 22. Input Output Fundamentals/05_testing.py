# There are 2 types of testing 
# 1) Manual testing
# We run code ourselves and check for errors and manual debug it

# 2) Automated test
# There are several automated test in python, some are 
# - assert 
# - unittest module

def add(a, b):
    return a + b

assert add(2, 3) == 5   # Test passed
assert add(1, 1) == 3   # Test failed

# We get an error message if test failed