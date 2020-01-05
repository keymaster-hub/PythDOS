from pathlib import Path
import sys
import os
import datetime


def dir():
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
        print(x.strftime('%m.%d.%Y  %H:%M'), dir_or_file, file_size, item)
    print(files_counter, 'файлов', summ_files_size)


def quit():
    # quit & exit commands
    sys.exit()


def tree(path='.', head='', tail=''):
    # DOS tree
    path = Path(path)

    if path.is_dir():
        print(head + path.name)
        entries = sorted(filter(Path.is_dir, path.iterdir()))

        for i, entry in enumerate(entries):
            if i < len(entries) - 1:
                tree(entry, tail + '├──', tail + '│  ')
            else:
                tree(entry, tail + '└──', tail + '   ')



