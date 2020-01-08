import re
import os


while True:
    cli = [ i for i in re.split(r'(^\w+)', (input(os.getcwd() + '>').lower())) if i]
    print(cli)
    
