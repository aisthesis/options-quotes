import re

def get_ticker(header):
    m = re.search('\((?P<ticker>[A-Z]*)\)\<\/', header)
    return m.group('ticker')

def get_quote_time_str(span_element):
    m = re.search('\>[A-Za-z]+ [0-9]+\, [0-9]\:[0-9]{2}[A-Z]{2} [A-Z]+\<', span_element)
    return m.group(0)[1:-1]
