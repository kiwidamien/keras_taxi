from itertools import zip_longest

CLIPPY = r"""/  \
|  |
@  @
|| ||  <--
|| ||
|\_/|
\___/     """

BLANK = '|' + ' '*70 + '|'

def clippify(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    if func.__doc__:
        doc_lines = [f'|{line:70s}|' for line in func.__doc__.split('\n')]
    else:
        doc_lines = ['| Nothing to see here|']

    doc_lines = ['-'*70 + '\\', BLANK, f'| It looks like you are trying to find help on {func.__name__:24s}|', BLANK] + doc_lines
    doc_lines = doc_lines + [BLANK, '-'*70 + '/']

    doc_string_lines = []
    for clip_line, doc_line in zip_longest(CLIPPY.split('\n'), doc_lines):
        if not clip_line:
            clip_line = ' ' * 10
        if not doc_line:
            doc_line = ' ' * 72
        doc_string_lines.append(f'{clip_line:10s} {doc_line:72s}')

    wrapper.__doc__ = '\n'.join(doc_string_lines)
    return wrapper
