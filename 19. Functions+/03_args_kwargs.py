def demo(*args, **kwargs):
    print("args:", args)      # → (1, 2, 3)
    print("kwargs:", kwargs)  # → {'name': 'Ali', 'age': 25}

demo(1, 2, 3, name="Ali", age=25)   