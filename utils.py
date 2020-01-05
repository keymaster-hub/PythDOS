from pathlib import Path
import sys


"""
-------------------quit-----------------------
"""
def quit():
    sys.exit()
    



"""
/------------------quit-----------------------
"""

"""
--------------------tree----------------------

"""
fork_string   = '|__'
corner_string = '|__'
wall_string   = '|  '
space_string  = '   '


def drawtree(path, seen, head='', tail=''):
    if path.exists():
        yield head + path.name

    if path.is_dir() and path.resolve() not in seen:
        seen.add(path.resolve())  # на случай зацикленных ссылок
        entries = sorted(path.iterdir(), key=lambda x: (x.is_file(), x.name))

        for i, entry in enumerate(entries):
            if i < len(entries) - 1:
                yield from drawtree(entry, seen, tail + fork_string, tail + wall_string)
            else:
                yield from drawtree(entry, seen, tail + corner_string, tail + space_string)


def tree(my_path='.'):
    for line in drawtree(Path(my_path), set()):
        print(line)

"""
/---------------------------tree--------------
"""

