import random
import string

import cmdline as cmd

BNAME_LEN = 30
FNAME_LEN = 30

REDIRECT = '/Users/ms2316/git_logs/log'

def win(prob):
    return (random.uniform(0,1) <= prob)

def random_string(sz):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=sz))

def gen_bname():
    return 'br_{}'.format(random_string(BNAME_LEN))

def grow_branch(bname, blen):
    cmd.branch_co(bname)
    cmd.make_commit('cmt')
    while (blen > 0):
        if win(0.3):
            cmd.make_commit('cmt')
            blen -= 1
        else:
            cmd.amend('amend')

def short_convergent():
    cmd.init_test()
    #init_configs()

    cmd.make_commit('root')
    for x in range(5):
        bname = gen_bname()
        blen = random.randint(2,10)

        cmd.branch_create(bname)
        grow_branch(bname, blen)
        cmd.branch_co('master')

        if win(0.2):
            cmd.merge(bname)
        else:
            cmd.branch_delete(bname)

        cmd.repo_size()

    cmd.finish_test()

short_convergent()
