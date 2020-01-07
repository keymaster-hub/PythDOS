from utils import *
import os
import re


ver = 'PythDOS [Version 0.0.3123]'
copyright = 'PythDOS, 2020. All rights reserved.'
print(ver)
print(copyright + '\n')

functions = {'tree': tree,
             'quit': quit, 'exit': quit, 'x': quit,
             'dir': dir, 'ls': dir,
             'cd': cd,
             'help': help, '?': help

             }

while True:
    cli = re.split(r'[/ ]', (input(os.getcwd() + '>').lower()), maxsplit=1)
    if str(cli[0]) in functions:
        if len(cli) > 1 and cli[1] == '?':
            print(functions[cli[0]].__doc__)
        else:   
            print('\n')
            functions[cli[0]](cli)
            print('\n')
