import utils
import os
import re


ver = 'PythDOS [Version 0.0.3123]'
copyright = 'PythDOS, 2020. All rights reserved.'
print(ver)
print(copyright + '\n')

functions = {'tree': utils.tree,
             'quit': utils.quit, 'exit': utils.quit, 'x': utils.quit,
             'dir': utils.dir, 'ls': utils.dir,
             'cd': utils.cd,
             'help': utils.help, '?': utils.help,
             'cls':utils.cls

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
