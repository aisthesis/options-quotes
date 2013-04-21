#! /usr/bin/env python3.3
import sys
import datetime

sys.path.append('../lib')
import extract
import util

DIRECTORY = '../data/'
# values to look for in file
TOP_ELEMENT_ID = 'rightcol'
COMPANY_ELEMENT_ID = 'yfi_rt_quote_summary'
COMPANY_INFO_TAG = 'h2'
QUOTE_TIME_ELEMENT_CLASS = 'time_rtq'
INPUT_DATE_FORMAT = '%b %d, %I:%M%p %Z'
FILE_OUTPUT_DATE_FORMAT = '%y%m%d-%H-%M'

# get input file name from command line
infile = DIRECTORY + sys.argv[1]

# load file content
content = ''
with open(infile, 'r') as f:
    content = f.read()

# strip to the part with the info needed
content = extract.get_element_by_attr('id', TOP_ELEMENT_ID, content)

company_info = extract.get_element_by_attr('id', COMPANY_ELEMENT_ID, content)
quote_time_str = extract.get_element_by_attr('class', QUOTE_TIME_ELEMENT_CLASS, company_info)
quote_time_str = util.get_quote_time_str(quote_time_str)
print(quote_time_str)
quote_time = datetime.datetime.strptime(quote_time_str, INPUT_DATE_FORMAT)
print(quote_time.strftime(FILE_OUTPUT_DATE_FORMAT))

company_info = extract.get_element_by_tag(COMPANY_INFO_TAG, company_info)
print(company_info)

ticker = util.get_ticker(company_info)
print(ticker)
