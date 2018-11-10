

# How is the chess board encoded ?
# 	- As a list
#
#	 0  1  2  3    <- List index is the row on the chess board
#	[2, 0, 3, 1]   <- Value in that list index is the column in which the queen is placed
#
# [2,0,3,1]
# Chess board will look like
# . . Q .
# Q . . .
# . . . Q
# . Q . .
#
# [1,2,3,4,0]
# Chess board will look like
# . Q . . .
# . . Q . .
# . . . Q .
# . . . . Q
# Q . . . .

# This function checks if no queen is in a check mate postion

import copy
import Permutate

def GoalTest(ChessBroard_Encoded):
	IsGoal = True
	i = 0

	for Queen in ChessBroard_Encoded:
		for nextQueen in ChessBroard_Encoded[i+1:]:
			if Queen == nextQueen:
				IsGoal = False
				break

		if IsGoal == False:
			break

		i = i + 1

		if i == len(ChessBroard_Encoded) - 1:
			break

	if IsGoal == True:
		i = 0
		for Queen in ChessBroard_Encoded:
			j = 0
			for nextQueen in ChessBroard_Encoded[i+1:]:
				j = j + 1
				if Queen == nextQueen - j or Queen == nextQueen + j:
					IsGoal = False
					break

			if IsGoal == False:
				break

			i = i + 1

			if i == len(ChessBroard_Encoded) - 1:
				break

	ChessBroard_Encoded_reversed = ChessBroard_Encoded[::-1]
	if IsGoal == True:
		i = 0
		for Queen in ChessBroard_Encoded_reversed:
			j = 0
			for nextQueen in ChessBroard_Encoded_reversed[i+1:]:
				j = j + 1
				if Queen == nextQueen - j or Queen == nextQueen + j:
					IsGoal = False
					break

			if IsGoal == False:
				break

			i = i + 1

			if i == len(ChessBroard_Encoded_reversed) - 1:
				break

	return IsGoal

# Decodes and prints the board
def printChessBoard(ChessBroard_Encoded, N):
	ChessBoradArray = [['.' for j in range(N)] for i in range(N)]

	Queen_rowNum = 0
	Queen_colNum = 0

	for Queen_rowNum in range(N):
		Queen_colNum = ChessBroard_Encoded[Queen_rowNum]
		ChessBoradArray[Queen_rowNum][Queen_colNum] = 'Q'

	for row in ChessBoradArray:
		strRow = ''
		for square in row:
			strRow = strRow + square + ' '

		print(strRow)

#N = Number of Queens

N = int(input("Number of Queens ? "))
ChessBroard_Encoded = [N-n-1 for n in range(N)]
print(ChessBroard_Encoded)
NumberOfSolutions = 0 

allCombinationsOfQueen = Permutate.generate_permutation_List(ChessBroard_Encoded)

for combinationX in allCombinationsOfQueen:
	if GoalTest(combinationX):
		NumberOfSolutions = NumberOfSolutions + 1
		print()
		print('Solution:',NumberOfSolutions, '___________________________')
		print(combinationX)
		printChessBoard(combinationX, N)
		print('________________________________________')

if(NumberOfSolutions != 0):
	pass
else:
	print('No Solution Found')


input('Press Enter to close')
