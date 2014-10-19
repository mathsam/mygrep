#!/usr/bin/env python
import RegExp
import unittest
import os
import sys
import testparser
#from poc import TemplateTestCase, Call, template

class TestRegExp(unittest.TestCase):
    """empty class, set up ty setattr later"""
    
def create_one_test(current_line):
    def test_regexp(self):
        regexp, stri, answer = testparser.test_parser(current_line)
        myregexp = RegExp.RegExp(regexp)
        match_position = myregexp.grep(stri)
        self.assertEqual(answer,match_position)
    return test_regexp

def create_multi_test(filename):
    file = open(filename)
    linenumber = 1 
    for current_line in file:
        test_method = create_one_test(current_line)
        test_method.__name__ = 'test_linenum_%d' %linenumber
        linenumber = linenumber + 1
        setattr(TestRegExp, test_method.__name__, test_method) 


if __name__ == "__main__":
    create_multi_test('cases') 
    unittest.main()
