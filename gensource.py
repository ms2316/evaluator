# Module for getting source code
import os
import random

path = '/Users/ms2316/linux_kernel/'
dirs = os.listdir(path)

def write_file():
    fname = random.choice(dirs)
    with open('{}{}'.format(path, fname), 'r') as f:
        max_lines = random.randint(1, 20)
        lines = f.read()
        print('echo {} > {} &&'.format(lines, fname))

write_file()
