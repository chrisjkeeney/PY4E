score = input("Enter Score: ")

try:
    fscore = float(score)
except:
    print("Please enter score between 0 and 1")
    quit()

if fscore >= .9:
    print('A')
elif fscore >= .8:
	print('B')
elif fscore >= .7:
	print('C')
elif fscore >= .7:
	print('D')
else:
    print('F')
