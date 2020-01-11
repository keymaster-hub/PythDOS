import utils
import os
import re


ver = 'PythDOS [Version 0.0.3123]'
copyright = 'PythDOS, 2020. All rights reserved.'
print(ver)
print(copyright + '\n')
allowed = [' ', '/', '>', '']

functions = {'tree': utils.tree,
             'quit': utils.quit, 'exit': utils.quit, 'x': utils.quit,
             'dir': utils.dir, 'ls': utils.dir,
             'cd': utils.cd, 'chdir':utils.cd,
             'help': utils.help, '?': utils.help,
             'cls':utils.cls,

             }



while True:
    input_string = input(os.getcwd() + '>').lower()
    cli = re.split(r'([a-zA-Z]+)(.*)', input_string)
    cli.append('')
    if str(cli[1]) in functions and (cli[2] == '' or str(cli[2])[0] in allowed):
        print('\n')
        functions[cli[1]](cli[2])
        print('\n')
    elif cli[1] != '': 
        print((*cli), """              не является внутренней или внешней
               командой, исполняемой программой или пакетным файлом.""")
