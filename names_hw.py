import re
pattern = re.compile("")
people = open("files/names.txt", "r").read()
lines = re.findall("[A-Z].+\n", people)

firstnames = []
lastnames = []
handles = []

for line in lines:
    sections = line.split('\t')
    firstnames.append(str((re.findall(", ([A-Z].+)", sections[0]))).strip("[]''"))
    lastnames.append(str((re.findall("^[A-Z]\w+", sections[0]))).strip("[]''"))
    if re.search('@', sections[-1]):
        handles.append(str((re.findall("(@\w+)", sections[-1]))).strip("[]''"))
    else:
        handles.append('')

print(f"=================== \nFull Name / Twitter \n===================")
        
lineCount = 0  
while lineCount < len(lines):
    print(f"{firstnames[lineCount]} {lastnames[lineCount]} / {handles[lineCount]}")
    lineCount += 1