#! /usr/bin/env python3.3
import sys
from datetime import datetime

sys.path.append('../lib')
import extract

DIRECTORY = '../data/'
# values to look for in file
TOP_ELEMENT_ID = 'yfncsumtab'
INNER_TABLE_CLASS = 'yfnc_datamodoutline1'
COLUMNS = 'Strike', 'Bid', 'Ask', 'Symbol', 'Last', 'Vol', 'Open Int'

# get command line info
equity = sys.argv[1]
expiration = sys.argv[2]
optiontype = sys.argv[3]

# construct input file name
infile = DIRECTORY + equity + expiration + '.html'
outfile = DIRECTORY + equity + expiration + optiontype + '.csv'

# load file content
content = ''
with open(infile, 'r') as f:
    content = f.read()

# strip to the part with the info needed
content = extract.get_element_by_attr('id', TOP_ELEMENT_ID, content)

# get the appropriate portion of the table (for now just the 'Call' table)
content = extract.get_element_by_attr('class', INNER_TABLE_CLASS, content)
content = extract.get_element_by_tag('table', content[6:-6])
html_rows = extract.get_rows(content)
header_row = extract.get_element_by_tag('tr', html_rows[0])
headers = extract.get_cell_contents(header_row, 'th')
rows = []
rows.append(headers)
for html_row in html_rows[1:]:
    rows.append(extract.get_cell_contents(html_row))

# write content to file
with open(outfile, 'w') as f:
    for row in rows:
        f.write(','.join(row) + '\n')

print("Content was written to file '{}'.".format(outfile))
