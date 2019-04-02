This defines a decorator in `clippify.py`. 

To use it:
```python
from clippify import clippify

@clippify
def say_hi(name):
  "Says hello to a person"
  return f'Hello, {name}'
```

This will modify the docstring.


Here is the sample output of `test.py`, which applies prints the docstring
of the function defined above.

```bash
➜  clippy git:(master) ✗ python test.py
/  \       ----------------------------------------------------------------------\ 
|  |       |                                                                      |
@  @       | It looks like you are trying to find help on say_hi                  |
|| ||  <-- |                                                                      |
|| ||      |Says hello to a person                                                |
|\_/|      |                                                                      |
\___/      ----------------------------------------------------------------------/ 
```

If you like this project, go ahead and give it a star!
