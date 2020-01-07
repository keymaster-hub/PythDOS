import os
import json

os.system('help>help.txt')
file = open('help.txt', mode='r', encoding='cp866')
command_list = [line.split(' ')[0] for line in file if line.split(' ')[0].isupper()]

help_dict = {}
remove = ['DISKPART', 'SC']
for command in command_list:
    if command not in remove:
        os.system(str(command) + '/? >command.txt')
        file = open('command.txt', mode='r', encoding='cp866')
        help_list = []
        for line in file:
            help_list.append(line.strip())
        help_dict[command] = help_list
        file.close()

filename = open('helpdb.txt', mode='w')
json.dump(help_dict, filename)
filename.close()
