import re

def retrieve(validator, prompt, errormsg):
    valid = re.compile(validator)
    while True:
        result = input(prompt)
        if valid.match(result):
            return result
        print(('\n' + errormsg).format(result))
