# Askhsh 1. Bingo 

from random import *

# Accumulative Mean
bingoSuccessAvg = 0;

#A Series of 1000 Bingo Games 
for g in range(1000) :

	# Bingo Game Start

	# 100 PLayers Select 5 Distinct Numbers Between 1 & 80

	# Creating Sets of Numbers Selected by 100 Players (Counting 0-99) 
	numberList = [[] for i in range(100)]
	numberSet = {}

	for x in range(100) :

		numberSet[x] = set() # Lists to Sets

		print('Player %d selected the numbers ' % (x+1) )	
		
		while len(numberSet[x]) < 5 :		# pick 5 distint Bingo Numbers
		
			selectedNum = randint(1,80) 			# random Number
			numberSet[x].add(selectedNum)			# add to the List
		
		print(*(numberSet[x]), sep = ", ") 


	# Create Bingo Set
	bingoNumSet = set()

	print('\nBINGO STARTS\n')

	bingoFlag = False

	while bingoFlag == False :
		
		bingoNum = randint(1,80) 			# draw of Bingo Number
		bingoNumSet.add(bingoNum)

		for x in range(100) :

			if numberSet[x].issubset(bingoNumSet) :
				print('BINGO! Player n.%d Wins with %d Numbers Drawn' % (x+1,len(bingoNumSet)))
				print("The Drawn Numbers Are ")
				print(*(bingoNumSet), sep = ", ")
				print('The Winning Numbers Are %s' % (numberSet[x]))
				print('\nGAME OVER\n')

				bingoFlag = True
				break

	bingoSuccessAvg += len(bingoNumSet)	# accumulate

bingoSuccessAvg = bingoSuccessAvg / 1000 # divide by 1000

print('For 1000 Bingo Games The Average Of BINGO Numbers Needed To Be Drawn Is %f' % (bingoSuccessAvg))				



