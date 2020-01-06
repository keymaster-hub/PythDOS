from utils import *
import os


ver = 'PythDOS [Version 0.0.3123]'
copyright = 'PythDOS, 2020. All rights reserved.'
print(ver)
print(copyright + '\n')

functions = {'tree':tree,
             'quit':quit, 'exit':quit, 'ex':quit,
             'dir':dir, 'ls':dir,
             'cd':cd,
             'help':help, '?':help
             
    }



while True:
    cli = []
    cli = [x for x in (input(os.getcwd() + '>').lower()).split(' ')]
    if str(cli[0]) in functions:
        print('\n')
        functions[cli[0]](cli)
        print('\n')
