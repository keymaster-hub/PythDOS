from utils import *
import os

ver = 'PythDOS [Version 0.0.3123]'
copyright = 'PythDOS, 2020. All rights reserved.'
print(ver)
print(copyright + '\n')

functions = {'tree':tree,
             'quit':quit, 'exit':quit,
             'dir':dir
             
    }

while True:

    cli = input(os.getcwd() + '>').lower()
    if cli in functions:
        print('\n')
        functions[cli]()
        print('\n')
