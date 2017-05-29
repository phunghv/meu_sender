#!/bin/python

import sys
import os
import re
from validate_email import validate_email

RECEIVER_FILE = "list_receivers.txt"

#
# Function load list of receiver from a file
# @param filename : Input file
# @return an array example ['a@email.com','b@email.com']
#
def load_receiver(filename):
    file = open(filename,'r')
    result = []
    lines = file.readlines()
    for line in lines:
        line = line.replace('\r','')
        line = line.replace('\n','')
        if validate_email(line):
            result.append(line)
    return result

def test():
    print "RUN TEST BEGIN"
    revs= load_receiver(RECEIVER_FILE)
    print revs
    print "RUN TEST END"


if __name__ == '__main__':
    try:
        #user_me = os.environ['MAIL_USER']
        #pass_me = os.environ['MAIL_PASS']
        #if user_me is None:
        #    print "Please set username and password"
        test()
    except IOError,e:
        print "Cannot load receiver file"
        print str(e)
    except Exception,e:
        print "Please set username and password"
        print str(e)
        sys.exit()
