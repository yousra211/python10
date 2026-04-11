from functools import partial

def greet(greeting, name):
    return f"{greeting}, {name}!"

say_hello = partial(greet, greeting="Hello")

print(say_hello(name="Alice"))  # "Hello, Alice!"
say_hello(name="Bob")    # "Hello, Bob!"