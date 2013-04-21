import re

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
    
    # Compile appropriate regular expressions
    opening_pattern = re.compile('\<' + tag + '[> ]')
    closing_pattern = re.compile('\<\/' + tag + '\>')

    # Get iterators over pattern matches
    opening_it = opening_pattern.finditer(content)
    closing_it = closing_pattern.finditer(content)
    
    try:
        mo = next(opening_it)
        mc = next(closing_it)
    except StopIteration:
        print("Invalid XML block!")
        raise

    try:
        mo = next(opening_it)
    except StopIteration:
        return content[:mc.end()]

    while mo.start() < mc.start():
        try:
            mo = next(opening_it)
        except StopIteration:
            try:
                mc = next(closing_it)
            except StopIteration:
                print("No closing tag found!")
                raise
            return content[:mc.end()]
        try:
            mc = next(closing_it)
        except StopIteration:
            print("No closing tag found!")
            raise
    return content[:mc.end()]

def get_element_by_attr(attr, attr_val, content):
    """Extract an element from a block of html code

    Retrieves the element identified by the attribute and value.
    Returns an empty string if no such element is found. If multiple
    elements with the given attribute and value are included in the content, 
    this function will return only the first one.

    Args:
        attr: The attribute for which to search
        attr_val: The value of the attribute for the desired element. For example,
            if attr_val is "blah" and attr is "id", the element retrieved will
            show in its opening tag id="blah"
        content: Content to search for the given attribute and value.

    Returns:
        A string containing the block of html for the desired element
    """
    start_index = content.find(' ' + attr + '="' + attr_val + '"')
    start_index = content[:start_index].rfind('<')
    return remove_after_close(content[start_index:])

def get_element_by_tag(tag, content):
    """Extract the first element with the given tag

    Retrieves the first element with the given tag specification

    Args:
        tag: XML tag of the element to extract
        content: XML string from which the tag is to be extracted

    Returns:
        A string containing the first block of XML with the given tag
    """
    m = re.search('\<' + tag + '[> ]', content)
    return remove_after_close(content[m.start():])
