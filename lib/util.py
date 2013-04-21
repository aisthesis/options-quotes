import re

def get_ticker(header):
    m = re.search('\((?P<ticker>[A-Z]*)\)\<\/', header)
    return m.group('ticker')
