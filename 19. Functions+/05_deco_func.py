# Decorator function with *args and **kwargs

def decorator_func(addition):
    def wrapper(*args, **kwargs):
        print("Function below performs addition!")
        addition(*args, **kwargs)
        print("Addition successfully performed!")
    return wrapper

@decorator_func
def addition(x, y):
    print(x + y)

addition(10, 5)