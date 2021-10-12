import re
with open("files/regex-test.txt") as names:
    for line in names.readlines():
        valid = re.match("([A-Z][a-z]+)( [A-Z][a-z]*){1,2}", line)
        if valid:
            print(valid.group())
        else:
            print(valid)
        
names.close()