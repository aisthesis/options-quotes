#! /usr/bin/env python3.3
import sys
sys.path.append('../lib')
import extract
import util

DIRECTORY = '../data/'
# values to look for in file
TOP_ELEMENT_ID = 'rightcol'
COMPANY_ELEMENT_ID = 'yfi_rt_quote_summary'
COMPANY_INFO_TAG = 'h2'

# get input file name from command line
infile = DIRECTORY + sys.argv[1]

# load file content
content = ''
with open(infile, 'r') as f:
    content = f.read()

# strip to the part with the info needed
content = extract.get_element_by_attr('id', TOP_ELEMENT_ID, content)

company_info = extract.get_element_by_attr('id', COMPANY_ELEMENT_ID, content)
company_info = extract.get_element_by_tag(COMPANY_INFO_TAG, company_info)
print(company_info)

ticker = util.get_ticker(company_info)
print(ticker)

#quote_time = extract.get_element_by_id()
