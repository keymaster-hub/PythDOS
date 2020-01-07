from pathlib import Path
import sys
import os
import datetime


def help(cli):
    if cli[0] == 'help' or cli[0] == '?':
        os.system('help>help.txt')
        file = open('help.txt', 'r', encoding='cp866')
        for line in file:
            print(line.strip())
    elif cli[1] == '?':
        os.system(str(cli[0]) + '/?>help.txt')
        file = open('help.txt', 'r', encoding='cp866')
        for line in file:
            print(line.strip())
        

def cd(cli):
    if len(cli) > 1:
        path = cli[1]
        if len(path) == 0 or Path(path).is_dir() == False:
            print(os.getcwd())
        else:
            accert: Path(path).is_dir()
            os.chdir(path)
    else:
        print(os.getcwd())

def dir(cli):
    print('Содержимое папки', os.getcwd())
    dir_count = 0
    files_counter = 0
    file_size = 0
    summ_files_size = 0
    for item in os.listdir('.'):
        if Path(item).is_dir():
            file_size = ''
            dir_or_file = '   <DIR>   '
            dir_count += 1
        else:
            dir_or_file = '           '
            file_size = os.stat(item).st_size
            summ_files_size += file_size
            files_counter += 1
        filetime = os.path.getmtime(item)
        x = datetime.datetime.fromtimestamp(filetime)
        print(x.strftime('%m.%d.%Y  %H:%M'), dir_or_file, '{:>10}'.format(file_size), item)
    print('{:>13}'.format(files_counter), 'файлов', summ_files_size, 'байт')


def quit(cli):
    # quit & exit commands
    sys.exit()


def tree(cli='', path='.', head='', tail=''):
    if 'f' in cli:
        print('files')
    cli = ''
    # DOS tree
    path = Path(path)
    if path.is_dir():
        print(head + path.name)
        entries = sorted(filter(Path.is_dir, path.iterdir()))

        for i, entry in enumerate(entries):
            if i < len(entries) - 1:
                tree(cli, entry, tail + '├──', tail + '│  ')
            else:
                tree(cli, entry, tail + '└──', tail + '   ')

