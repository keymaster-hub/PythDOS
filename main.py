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
    cli.append(' ')
    cli.append(' ')
    function_name = cli[1]
    argument = cli[2].strip()
    if function_name in functions and (argument == '' or (argument[0] in allowed)\
       and len(argument) > 1):
        functions[function_name](argument)
    elif function_name != ' ': 
        print(function_name, """ не является внутренней или внешней
командой, исполняемой программой или пакетным файлом.""")
