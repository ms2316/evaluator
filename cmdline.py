# Command line interface module

def repo_size(redir):
    print('gdu -bs .git/objects >> {} &&'.format(redir))
    print('echo ----------- >> {} &&'.format(redir))

def make_commit(msg):
    print('git add . && git commit -m "{}" && '.format(msg))

def amend(msg):
    print('git add . && git commit --amend -m "{}" && '.format(msg))

def branch_create(bname):
    print('git branch {} && '.format(bname))

def branch_delete(bname):
    print('git branch -D {} && '.format(bname))

def branch_co(bname):
    print('git checkout {} &&'.format(bname))

def merge(bname):
    print('git merge {} &&'.format(bname))

def init_test():
    print ("#!/bin/sh\n"
           "#\n"
           "# Copyright (c) 2018 Mihails Smolins\n"
           "#\n\n"
           "test_description='evaluation'\n\n"
           ". ./test-lib.sh\n\n"
           "test_expect_success 'pre-test setup' '\n"
           'GIT_AUTHOR_DATE="2006-06-26 00:00:00 +0000" &&\n'
           'GIT_COMMITTER_DATE="2006-06-26 00:00:00 +0000" &&\n'
           "export GIT_AUTHOR_DATE GIT_COMMITTER_DATE\n"
           "'\n\n"
           "test_expect_success 'evaluation' '")

def init_configs():
    print('git config --global gc.auto 0 &&')

def finish_test():
    print('echo Done')
    print("'\n\ntest_done")
