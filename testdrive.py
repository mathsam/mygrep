#!/usr/bin/env python
import RegExp
import os
import sys
import testparser
import nose

def gen_test():
    file = open('cases',mode='r')
    for current_line in file:
#        print >> sys.stdout, current_line
#        regexp, stri, answer = testparser.test_parser('<x><x><[x]>')
        yield check_regexp, current_line 

def check_regexp(current_line):
    print >> sys.stdout, current_line
    regexp, stri, answer = testparser.test_parser(current_line)
    myregexp = RegExp.RegExp(regexp)
    match_position = myregexp.grep(stri)
    assert answer == match_position
            

if __name__ == "__main__":
    nose.main()
