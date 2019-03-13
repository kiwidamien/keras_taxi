from clippify import clippify

@clippify
def say_hi(name):
    "Says hello to a person"
    return f'Hello, {name}'

@clippify
def f():
    """
    This is a function

    The docstring is long

    Like......
    really long

    So many lines
    No real reason for it to be as long as it is

    No real point to this function

    Inputs
    ------
    None

    Outputs
    -------
    Answer to Life, the Universe and Everything:: integer

    Raises
    ------
    Does not raise any exceptions
    """
    return 42


if __name__ == '__main__':
    print(say_hi.__doc__)
    print(f.__doc__)
