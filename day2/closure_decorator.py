def sum(x):
    if(x is None):
        return x
    def inner_func(y):
        return x+y
    return inner_func
result = sum(10)(20)
print(result)


def added(func):
    def inner_func(name):
        if not name:
            print("Name field is required")
        else:
            func(name)
    return inner_func
@added
def login(name):
    print(f"Hello {name}")

login("rojitha")
login("")
