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
    string = ' '
    cli = ['']
    input_string = input(os.getcwd() + '>').lower()
    if len(input_string) > 0:
        string = re.match(r'([a-zA-Z]+)(.*)', input_string)
        cli = list(string.groups())
    if str(cli[0]) in functions and (cli[1] == '' or str(cli[1])[0] in allowed):
        print('\n')
        functions[cli[0]](cli[1])
        print('\n')
    elif len(cli) > 1:
        print((*cli), """              не является внутренней или внешней
               командой, исполняемой программой или пакетным файлом.""")
