# Module for getting source code

import os
import random

path = '/Users/ms2316/linux_kernel/'
dirs = os.listdir(path)
chars = ['"', "'", '(', ')', '{', '}', '[', ']', '-']
LINELIMIT = 5

'''Picks a random file from linux kernel and
prints its content redirecting to a specific file
'''
def write_file():
    # choose file randomly
    fname = random.choice(dirs)
    with open('{}{}'.format(path, fname), 'r', encoding='ISO-8859-1') as f:
        lines = f.read().splitlines()
        start = random.randint(0, len(lines)-1)
        finish = random.randint(start, len(lines)-1)
        # take random number of consecutive lines of code
        if (start + LINELIMIT < finish):
            finish = start + LINELIMIT
        code = lines[start:finish+1]
        for line in code:
            #il = line.replace("'","").replace('"', '').replace('`', '') \
            #        .replace('(',' ').replace(')',' ').replace('[', '')
            l = line
            for ch in chars:
                l = l.replace(ch, '')

            print('echo " {} " >> {} &&'.format(l, fname))
            #print('printf "\\n" >> {} &&'.format(fname))

