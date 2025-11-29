# *args lets a Python function accept any number of positional arguments. 
# When you use *args in a function definition, all extra arguments passed to the function are collected into a tuple, 
# which you can then loop through or use
# No need to predefine arguments

# *args makes tuple


def args_function(*nums):
    
    print(nums)

args_function('Vansh', 10)
