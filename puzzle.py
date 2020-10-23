import copy

def LoadFromFile(filepath):
	board_list = []
	n = 0
	with open(filepath, 'r') as f:
		count = 0
		for line in f:
			line_list = []
			if count == 0:
				n = f
			else:
				row = line.strip().split("\t")
				for item in row:
					if item == "*":
						line_list.append("0")
					else:
						line_list.append(item)
				board_list.append(line_list)
			count+=1
	return board_list

"""
def IfFileIsNotCoolAndEpic:
	pass
"""

def DebugPrint(state):
	for i in state:
		funny_dog_really_funny = ""
		for j in i:
			funny_dog_really_funny += j + "\t"
		print(funny_dog_really_funny)

def FindZeroCoord(state):
	for i in range(len(state)):
		for j in range(len(state)):
			if state[i][j] == "0":
				return tuple([i, j])

#CHANGE
def swap(state, ZeroCoords, SwapCoords):
	newState = copy.deepcopy(state)
	zero_row, zero_col = ZeroCoords
	swap_row, swap_col = SwapCoords
	newState[zero_row][zero_col], newState[swap_row][swap_col] = newState[swap_row][swap_col], newState[zero_row][zero_col]
	return newState


def ComputeNeighbors(state):
	return_val = []
	ZeroCoords = FindZeroCoord(state)
	print(ZeroCoords)
	row,col = ZeroCoords
	#check above 
	if row - 1 >= 0:
		return_val.append([state[row - 1][col], swap(state, ZeroCoords, (row - 1, col))])
	#below
	if row + 1 <= len(state) -1:
		return_val.append([state[row + 1][col], swap(state, ZeroCoords, (row + 1, col))])
	#left
	if col - 1 >= 0:
		return_val.append([state[row][col - 1], swap(state, ZeroCoords, (row, col - 1))])
	#right
	if col + 1 <= len(state) -1:
		return_val.append([state[row][col + 1], swap(state, ZeroCoords, (row, col + 1))])
	
	return tuple(return_val)

def isGoal(state):
	index = 0
	n = len(state)
	for i in range(n):
		for j in range(n):
			print(int(state[i][j]))
			if not int(state[i][j]) == index + 1:
				return False
			if i == n-1 and j == n-2:
				return True
			index += 1


DebugPrint(LoadFromFile("testcase.txt"))					# TEST LoadFromFile
print(ComputeNeighbors(LoadFromFile("testcase.txt")))		# TEST ComputeNeighbors
print(isGoal(LoadFromFile("testcasetwo.txt")))				# TEST isGoal