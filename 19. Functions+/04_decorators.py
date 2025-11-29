# Decorators in functions add extra behaviour in function without changing its code
# Does extra work before / after the function
# Type of wrapping

def deco(func):
    def wrapper():
        print('Statement printed before function')
        func()
        print('Statement printed after function')
    return wrapper

@deco
def func():
    print('Hello!')

func()