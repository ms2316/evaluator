# Helper module

import random
import string

BNAME_LEN = 30

def win(prob):
    return (random.uniform(0,1) <= prob)

def random_string(sz):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=sz))

def gen_bname():
    return 'br_{}'.format(random_string(BNAME_LEN))
