# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
tot = None
count = None
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    if count is None:
        count = 1
    else:
        count = count + 1
    number = line.find('0')
    number = line[number:]
    n = float(number)
    if tot is None:
        tot = n
    else:
    	tot = tot + n
avg = tot/count
print("Average spam confidence:",avg)
