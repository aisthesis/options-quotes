#! /usr/bin/env python3.3
import sys
DIRECTORY = '../data/'
# values to look for in file
ELEMENT_ID = 'rightcol'

# get input file name from command line
infile = DIRECTORY + sys.argv[1]

# load file content
content = ''
with open(infile, 'r') as f:
    content = f.read()

def get_element_by_id(element_id, content):
    """Extract an element from a block of html code

    Retrieves the element identified by the given element_id.
    Returns an empty string if no such element is found. If multiple
    elements with the given id are included in the content, this function
    will return only the first one.

    Args:
        element_id: The id of the desired element. For example,
            if element_id is "blah", the element retrieved will
            show in its opening tag id="blah"
        content: Content to search for the given element_id

    Returns:
        A string containing the block of html for the desired element
    """
    start_index = content.find('id="' + ELEMENT_ID + '"')
    start_index = content[:start_index].rfind('<')
    content = content[start_index:]
    tag_end = content.find(' ')
    tag = content[1:tag_end]
    print('tag is "' + tag + '"')

get_element_by_id(ELEMENT_ID, content)
