


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


def IfFileIsNotCoolAndEpic
	pass

def DebugPrint(state):
	for i in state:
		funny_dog_really_funny = ""
		for j in i:
			funny_dog_really_funny += j + "\t"
		print(funny_dog_really_funny)

def henrysdumbfunction(state):
	Zero_Coord = []
	for row in state:
		for item in row:
			if item == "0":
				Zero_Coord.append(row)
				Zero_Coord.appead(item)
	return tuple(Zero_Coord)

def ComputeNeighbors(state):
	Zero_Coord = henrysdumbfunction(state)
	n = len(state)

	


	return pairs


DebugPrint(LoadFromFile("testcase.txt"))
