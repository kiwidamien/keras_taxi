from clippify import clippify

@clippify
def say_hi(name):
    "Says hello to a person"
    return f'Hello, {name}'

if __name__ == '__main__':
    print(say_hi.__doc__)
