from utils import *
import sys


functions = {'tree':tree, 'quit':quit, 'exit':quit
    }

while True:

    f = input('C:\\_')
    if f in functions:
        functions[f]()

    
