#! /usr/bin/env python3.3
import sys
sys.path.append('../lib')
import extract

DIRECTORY = '../data/'
# values to look for in file
ELEMENT_ID = 'rightcol'

# get input file name from command line
infile = DIRECTORY + sys.argv[1]

# load file content
content = ''
with open(infile, 'r') as f:
    content = f.read()

print(extract.get_element_by_id(ELEMENT_ID, content))
