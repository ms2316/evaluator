import random
import string

BNAME_LEN = 30
FNAME_LEN = 30

def win(prob):
    return (random.uniform(0,1) <= prob)

def random_string(sz):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=sz))

def write_file():
    rstring = random_string(FNAME_LEN)
    print('echo {} > f_{} && '.format(rstring, rstring))

def repo_size():
    print('gdu -bs .git/objects >> /Users/ms2316/eval_log &&')

def make_commit(msg):
    write_file()
    print('git add . && git commit -m "{}" && '.format(msg))

def amend(msg):
    write_file()
    print('git add . && git commit --amend -m "{}" && '.format(msg))

def gen_bname():
    return 'br_{}'.format(random_string(BNAME_LEN))

def branch_create(bname):
    print('git branch {} && '.format(bname))

def branch_delete(bname):
    print('git branch -D {} && '.format(bname))

def branch_co(bname):
    print('git checkout {} &&'.format(bname))

def merge(bname):
    print('git merge {} &&'.format(bname))

def grow_branch(bname, blen):
    branch_co(bname)
    make_commit('cmt')

    while (blen > 0):
        if win(0.5):
            make_commit('cmt')
            blen -= 1
        else:
            amend('amend')

def init_configs():
    print('git config --global gc.auto 0 &&')

def init_test():
    print('#!/bin/sh\n#\n# Copyright (c) 2018 Mihails Smolins\n#\n')
    print("test_description='evaluation'\n")
    print('. ./test-lib.sh')
    print("test_expect_success 'evaluation' '")

def finish_test():
    print('echo DONE')
    print("'\n")
    print('test_done')

def short_convergent():
    init_test()
    init_configs()

    make_commit('root')
    for x in range(20):
        bname = gen_bname()
        blen = random.randint(2,10)

        branch_create(bname)
        grow_branch(bname, blen)
        branch_co('master')

        if win(0.5):
            merge(bname)
        else:
            branch_delete(bname)

        repo_size()

    finish_test()

short_convergent()


