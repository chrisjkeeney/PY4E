import re
hand = open('regex.txt')

numlist = list()
for line in hand:
    line = line.rstrip()
    reg = re.findall('[0-9]+', line)
    if len(reg) != 1: continue
    num = int(reg[0])
    numlist.append(num)
print('Sum is: ', sum(numlist))
