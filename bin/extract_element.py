#! /usr/bin/env python3.3
import sys
import re

DIRECTORY = '../data/'
# values to look for in file
ELEMENT_ID = 'rightcol'

# get input file name from command line
infile = DIRECTORY + sys.argv[1]

# load file content
content = ''
with open(infile, 'r') as f:
    content = f.read()

def remove_after_close(content):
    """Return content trimmed after the opening tag has been closed

    Finds the close of the first XML tag found and strips all 
    subsequent content.

    Args:
        content: the content to be searched

    Returns:
        The trimmed content string
    """
    # Basic validation
    assert content.startswith('<')
    assert '>' in content

    # Determine tag to look for
    tag_end = content.find('>')
    tag = content[1:tag_end]
    tag = tag.split()[0]
    
    # Set up a net count for opening and closing tags
    net_tag_count = 1
    current_index = len(tag)
    opening_pattern = re.compile('\<' + tag + '[> ]')
    matches = opening_pattern.findall(content)
    print("%d opening matches found." % len(matches))
    closing_pattern = re.compile('\<\/' + tag + '\>')
    closing_matches = closing_pattern.findall(content)
    print("%d closing matches found." % len(closing_matches))
    for m in closing_matches:
        print(m)
    closing_str = '</' + tag + '>'
    end_index = 0
    #while net_tag_count > 0:
        

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
    return remove_after_close(content[start_index:])

get_element_by_id(ELEMENT_ID, content)
#remove_after_close('<blah this is cra-cra!> ')