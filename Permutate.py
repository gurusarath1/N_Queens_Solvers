# Code Written by Guru Sarath
# Date: Nov 6 2018

# Generates all permutations of elements in a list

# Usage -
# x = generate_permutation_List([1,2,3,4,5,6])
# x will contain all permutations

"""

Working of algorithm

Level -1 --------------------------------------------------------------------------------------------------------

                        generate_permutation_List([1,2,3,4,5,6])
						
						             |
									 |
									 |
									 
	permutateList(inputSequence_2, ['.' for n in inputSequence_2], printOutput, stringFormatOutput, [-1], fullOutputList)

Level 0 ---------------------------------------------------------------------------------------------------------

iteration order -                                  123
count of elements -                                111
elements -                                         ABC
output list -                                     (...)
 
Level 1 ---------------------------|-------------------------------|---------------------------------------------
                                   |                               |
                     12            |             1 2               |            12
                    011            |             101               |            110
                    ABC            |             ABC               |            ABC
                   (A..)           |            (B..)              |           (C..)
				                   |                               |
Level 2 ---------------------------|-------------------------------|----------------------------------------------
                                   |                               |
                  1          1     |       1             1         |     1               1                
                001         010    |     001             100       |    010              100
                ABC         ABC    |     ABC             ABC       |    ABC              ABC
               (AB.)       (ACC)   |    (BA.)           (BCC)      |   (CA.)            (CBB)
                                   |                               |
Level 3 ---------------------------|-------------------------------|----------------------------------------------
                                   |                               |
                000         000    |     000             000       |    000              000
				ABC         ABC    |     ABC             ABC       |    ABC              ABC
               (ABC)       (ACB)   |    (BAC)           (BCA)      |   (CAB)            (CBA)
                                   |                               |
                                   |                               |
								   
"""



import copy

#use this function in your code
def generate_permutation_List(inputSequence, printOutput = False, stringFormatOutput = False):
	fullOutputList = list()
	inputSequence_2 = [[x, 1] for x in inputSequence] #List 
	permutateList(inputSequence_2, ['.' for n in inputSequence_2], printOutput, stringFormatOutput, [-1], fullOutputList)
	return fullOutputList

	
#permutateList function generates all permutations
#FullOutputlist is the actual return value
def permutateList(inputSequence_2, output_list, printOutput, stringFormatOutput, level, FullOutputlist):

	#We are entering a level deep
	level[0] = level[0] + 1

	#print('Level - ', level[0], inputSequence_2, output_list)
	
	allCountsZeroFlag = True

	#Check if all the counts of elements in the list is zero
	for ele in  inputSequence_2:
		if ele[1] >= 1:
			allCountsZeroFlag = False

	#End of recursion - Return the combination generated (We are in level N)
	if allCountsZeroFlag:
		FullOutputlist.append(copy.deepcopy(output_list))

		if stringFormatOutput and printOutput:
			print(ListToString(output_list)) #Print output as a string
		elif printOutput:
			print(output_list) #Print output as list
		else:
			pass #Do nothing
			
		level[0] = level[0] - 1
		return #Go back to previous level

	i = -1
	for element in inputSequence_2:
		i = i + 1
		#If element's count is greater than 1 
		#Decrement the element's count and goto next level
		if element[1] >= 1:
			inputSequence_2X = copy.deepcopy(inputSequence_2)
			inputSequence_2X[i][1] = inputSequence_2X[i][1] - 1
			output_list[level[0]] = inputSequence_2X[i][0]
			if level[0] < len(inputSequence_2X):
				permutateList(inputSequence_2X, output_list, printOutput, stringFormatOutput, level, FullOutputlist)
	
	level[0] = level[0] - 1
	return #Go back to previous level


#Converts elements of list to a single continuous list 
def ListToString(listX):
	strX = ''

	if listX != None:
		for ele in listX:
			strX = strX + str(ele)

	return strX