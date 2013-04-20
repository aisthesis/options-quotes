#! /usr/bin/env python3.3
import sys
DIRECTORY = 'tmp/'
# values to look for in file
BODY_ID = 'rightcol'
BODY_TAG = 'div'

# get input file name from command line
infile = DIRECTORY + sys.argv[1]

# load file content
content = ''
with open(infile, 'r') as f:
    content = f.read()
print(content)
