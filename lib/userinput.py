import re

def retrieve(validator, prompt, errormsg):
    valid = re.compile(validator)
    while True:
        result = input("\n{}".format(prompt))
        if valid.match(result):
            break
        print(errormsg.format(result))
    return result
