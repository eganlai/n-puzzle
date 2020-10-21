
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
				row = line.split("\t")
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
	Zero_Coord = []
	for row in state:
		for item in row:
			if item == "0":
				Zero_Coord.extend([row, item])
	return tuple(Zero_Coord)

def swap(state, ZeroCoords, SwapCoords):
	copy = ZeroCoords
	state[ZeroCoords[0]][ZeroCoords[1]] = state[SwapCoords[0]][SwapCoords[1]]
	state[SwapCoords[0]][SwapCoords[1]] = state[copy[0]][copy[1]]
	return state


def ComputeNeighbors(state):
	return_val = []
	ZeroCoords = FindZeroCoord(state)
	#check above 
	if int(ZeroCoords[0]) - 1 >= 0:
		return_val.append([int(ZeroCoords[0]) - 1, swap(state, ZeroCoords, tuple(str(int(ZeroCoords[0]) - 1), ZeroCoords[1]))])
	#below
	if int(ZeroCoords[0]) + 1 <= len(state) -1:
		return_val.append([int(ZeroCoords[0]) + 1, swap(state, ZeroCoords, tuple(str(int(ZeroCoords[0]) + 1), ZeroCoords[1]))])
	#left
	if int(ZeroCoords[1]) - 1 >= 0:
		return_val.append([])
	#right
	if int(ZeroCoords[1]) + 1 <= len(state) -1:
	#HELPHELPHELPHELPHELPHELPHELPHELPHELPHELPHELPHELPHELPHELPHELPHELP

	return tuple(return_val)



DebugPrint(LoadFromFile("testcase.txt"))
print(computeNeighbors(LoadFromFile("testcase.txt")))
