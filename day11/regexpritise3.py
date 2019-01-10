import re

arg1 = input('Please input your strings: ')
arg2 = input('Please input character you want to delete: ')

def newstrip(arg1,arg2):
    if arg2 == None:
        args = r'\s'
    newRegex = re.compile(arg2)
    print(newRegex.sub('',arg1))

newstrip(arg1,arg2)