import re

def retrieve(validator, prompt, errormsg):
    valid = re.compile(validator)
    while True:
        result = input(prompt)
        if valid.match(result):
            break
        print(('\n' + errormsg).format(result))
    return result
