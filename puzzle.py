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
				board_list.append(tuple(line_list))
			count+=1
	return tuple(board_list)

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
	newState = list(list(row) for row in copy.deepcopy(state))
	zero_row, zero_col = ZeroCoords
	swap_row, swap_col = SwapCoords
	newState[zero_row][zero_col], newState[swap_row][swap_col] = newState[swap_row][swap_col], newState[zero_row][zero_col]
	return tuple(tuple(row) for row in newState)


def ComputeNeighbors(state):
	return_val = []
	ZeroCoords = FindZeroCoord(state)
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
	
	return return_val

def IsGoal(state):
	index = 0
	n = len(state)
	for i in range(n):
		for j in range(n):
			# print(int(state[i][j]))
			if not int(state[i][j]) == index + 1:
				return False
			if i == n-1 and j == n-2:
				return True
			index += 1

def BFS(state):
	frontier = [(0, state)]
	discovered = set(state)
	parents = {(0, state): None}
	path = []
	while len(frontier) != 0:
		current_state = frontier.pop(0)
		discovered.add(current_state[1])
		if IsGoal(current_state[1]):
			while parents.get((current_state[0], current_state[1])) != None:
				path.insert(0, current_state[0])
				current_state = parents.get((current_state[0], current_state[1]))
			return path
		for neighbor in ComputeNeighbors(current_state[1]):
			if neighbor[1] not in discovered:
				frontier.append(neighbor)
				discovered.add(neighbor[1])
				parents.update({(neighbor[0], neighbor[1]): current_state})
	print("--FAIL--")
	return None

def DFS(state):
	frontier = [(0, state)]
	discovered = set(state)
	parents = {(0, state): None}
	path = []
	while len(frontier) != 0:
		current_state = frontier.pop(0)
		discovered.add(current_state[1])
		if IsGoal(current_state[1]):
			while parents.get((current_state[0], current_state[1])) != None:
				path.insert(0, current_state[0])
				current_state = parents.get((current_state[0], current_state[1]))
			return path
		for neighbor in ComputeNeighbors(current_state[1]):
			if neighbor[1] not in discovered:
				frontier.insert(0, neighbor)
				discovered.add(neighbor[1])
				parents.update({(neighbor[0], neighbor[1]): current_state})
	print("--FAIL--")
	return None
def BidirectionalSearch(state):
	pass
'''
DebugPrint(LoadFromFile("testcasetwo.txt"))					# TEST LoadFromFile
print(ComputeNeighbors(LoadFromFile("testcasetwo.txt")))		# TEST ComputeNeighbors
print(IsGoal(LoadFromFile("testcasetwo.txt")))				# TEST isGoal
'''
print(BFS(LoadFromFile("testcase.txt")))