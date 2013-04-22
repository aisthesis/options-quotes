#! /usr/bin/env python3.3
import sys
import os
import re
import http.client

sys.path.append('../lib')
import extract
import userinput

HTTP_SERVER = 'finance.yahoo.com'
URL_TEMPLATE = '/q/op?s={}&m={}'
# values to look for in markup
TOP_ELEMENT_ID = 'yfncsumtab'
INNER_TABLE_CLASS = 'yfnc_datamodoutline1'
# tab-delimited because fields may contain ','
DELIMITER = '\t'
OUTFILE_EXTENSION = '.tsv'
DIRECTORY = '../data/'

user = os.environ.get('USER', 'Investor')
print("\nHello, {}, this script will retrieve options quotes from Yahoo!\n".format(user))

# Prompt for required user input
# equity
validator = '[a-zA-Z]{1,6}$'
prompt = 'Enter equity ticker: '
errormsg = "'{}' is not a valid ticker! Please try again."
equity = userinput.retrieve(validator, prompt, errormsg)
print("Equity is '{}'.\n".format(equity))

# expiration
validator = '2[0-9]{3}\-[0-9]{2}$'
prompt = "Enter expiration month in the format YYYY-MM (e.g. '2013-05'): "
errormsg = "'{}' is not a valid expiration! Please try again."
expiration = userinput.retrieve(validator, prompt, errormsg)
print("Expiration is '{}'.\n".format(expiration))

# option type (call or put)
validator = '[CP]'
prompt = "Enter 'C' for Calls or 'P' for Puts: "
errormsg = "'{}' is not a valid option type abbreviation! Please try again."
optiontype = userinput.retrieve(validator, prompt, errormsg)
print("Option type is '{}'.\n".format(optiontype))

# Open http connection to retrieve data
conn = http.client.HTTPConnection(HTTP_SERVER)
conn.request("GET", URL_TEMPLATE.format(equity, expiration))
r = conn.getresponse()
data = r.read()
conn.close()
content = data.decode()

# strip to the part with the info needed
content = extract.get_element_by_attr('id', TOP_ELEMENT_ID, content)

# get the appropriate portion of the table
# go to second inner table for puts
if optiontype == 'P':
    start = content.find('class="{}"'.format(INNER_TABLE_CLASS))
    content = content[start:]
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
outfile = DIRECTORY + equity + expiration + optiontype + OUTFILE_EXTENSION
with open(outfile, 'w') as f:
    for row in rows:
        f.write(DELIMITER.join(row) + '\n')

print("Quotes were written to file '{}'.".format(outfile))
