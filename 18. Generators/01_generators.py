# Generator is a function which gives value one by one not all at once
# These use less memory 

def my_gen():
    yield 1
    yield 2
    yield 3

g = my_gen()
print(next(g))