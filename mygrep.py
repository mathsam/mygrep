#!/usr/bin/env python
import RegExp   as rp
import bcolors  as bc
import sys

def match_and_print(regexp,filename):
    file = open(filename,mode='r')
    matcher = rp.RegExp(regexp)
    linenumber = 1
    for line in file:
        result = matcher.grep(line)
        if(result):
            print >> sys.stdout, '%04d: %s%s%s%s%s' \
                      %(linenumber, line[0:result[0]],\
                        bc.bcolors.WARNING, line[result[0]:result[1]+1], bc.bcolors.ENDC,\
                        line[result[1]+1:-1])
        linenumber = linenumber + 1
    file.close()

def main():
    if len(sys.argv) <= 2:
        print >> sys.stderr, 'Usage: %s RegExp filename[s]' % sys.argv[0]
    else:
        for filename in sys.argv[2:]:
            print >> sys.stdout, '----------------------------------------------\n' \
            'In file: %s' %filename
            match_and_print(sys.argv[1], filename)


if __name__ == "__main__":
    main()
