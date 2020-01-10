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
             'cd': utils.cd, 'chdir':utils.cd,
             'help': utils.help, '?': utils.help,
             'cls':utils.cls,

             }


while True:
    string = re.match(r"([a-zA-Z]+)(.*)", (input(os.getcwd() + '>').lower()))
    cli = list(string.groups())
    if str(cli[0]) in functions:
        print('\n')
        functions[cli[0]](cli[1])
        print('\n')
