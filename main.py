import utils
import os
import re
from contextlib import redirect_stdout

ver = 'PythDOS [Version 0.0.3123]'
copyright = 'PythDOS, 2020. All rights reserved.'
print(ver)
print(copyright + '\n')

functions = {'tree': utils.tree,
             'quit': utils.dos_quit, 'exit': utils.dos_quit, 'x': utils.dos_quit,
             'dir': utils.dos_dir, 'ls': utils.dos_dir,
             'cd': utils.dos_cd, 'chdir': utils.dos_cd,
             'help': utils.dos_help, '?': utils.dos_help,
             'cls': utils.dos_cls,
             'type': utils.dos_type,
             'del': utils.dos_del, 'erase': utils.dos_del,
             'rmdir': utils.dos_rmdir, 'rd': utils.dos_rmdir,
             'mkdir': utils.dos_mkdir, 'md': utils.dos_mkdir,
             'rename': utils.dos_rename, 'ren': utils.dos_rename,
             'copy': utils.dos_copy,
             'move': utils.dos_move
             }

while True:
    input_string = input(os.getcwd() + '>').lower()
    cli = re.split(r'([a-z]+)(.*)', input_string)
    cli.extend(' '' ')
    function_name = cli[1]
    argument = cli[2]
    if function_name in functions and argument == '/?':
        print(functions[function_name].__doc__)
    elif function_name in functions and (len(argument) and '>' in argument):
        file_name = argument[argument.rfind('>')+1:]
        argument = argument[:argument.rfind('>')]
        with open(file_name, 'w') as file:
            with redirect_stdout(file):
                if argument == '/?':
                    print(functions[function_name].__doc__)
                else:
                    functions[function_name](argument)
    elif function_name in functions:
        functions[function_name](argument.strip())
        print('\n')
    elif input_string.strip() == '':
        pass
    else:
        print(input_string, """ не является внутренней или внешней
командой, исполняемой программой или пакетным файлом.""")
