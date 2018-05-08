import random

import cmdline as cmd
import gensource as gen
import helper as h

REDIRECT = '/Users/ms2316/git_logs/log'

def grow_branch(bname, blen):
    cmd.branch_co(bname)
    gen.write_file()
    cmd.make_commit('cmt')
    while (blen > 0):
        gen.write_file()
        if h.win(0.3):
            cmd.make_commit('cmt')
            blen -= 1
        else:
            cmd.amend('amend')
            cmd.repo_size(REDIRECT)

def short_convergent():
    cmd.init_test()
    #init_configs()

    gen.write_file()
    cmd.make_commit('root')
    for x in range(5):
        bname = h.gen_bname()
        blen = random.randint(2,10)

        cmd.branch_create(bname)
        grow_branch(bname, blen)
        cmd.branch_co('master')

        if h.win(0.2):
            cmd.merge(bname)
        else:
            cmd.branch_delete(bname)

        cmd.repo_size(REDIRECT)

    cmd.finish_test()

short_convergent()


