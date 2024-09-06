import sys

inputfile = sys.argv[1]

f = open(inputfile, 'r', encoding="utf8")
fileData = f.read()
splitData = fileData.split('\n')
f.close()


writeData = ''
i = 0
numLines = len(splitData)
print(numLines)
while i < numLines:
    line = splitData[i]
    if len(line) > 0 and line[0] > chr(0x7F):
        line = line.replace(' ', '')
    print(line)
    writeData += line + "\n"
    i += 1
    
f = open(inputfile, 'w', encoding="utf8")
f.write(writeData)
f.close()

##print("split data" + ''.join(splitData))