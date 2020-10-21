
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
				Zero_Coord.extend([row, item])
	return tuple(Zero_Coord)

def swap(state, ZeroCoords, SwapCoords):
	copy = ZeroCoords
	state[ZeroCoords[0]][ZeroCoords[1]] = state[SwapCoords[0]][SwapCoords[1]]
	state[SwapCoords[0]][SwapCoords[1]] = state[copy[0]][copy[1]]
	return state

def computeNeighbors(state):
    hole_coords = [0,0]
    adjacent_coords = []
    for y in range(len(state)):
        for x in range(len(state[y])):
            if state[y][x] == "*": 
                hole_coords[0] = x
                hole_coords[1] = y     
    adjacent_coords = checkNext(state, hole_coords)
    final_list = []
    state_modified = []
    original = []
    location = 0
    location2 = 0
    for y in state:
        for x in y: 
            if x != "*":
                state_modified.append(x)
                original.append(x)
            else:
                state_modified.append("*")
                original.append("*")
    #for loop to return from computeNeighbors properly            
    for y in range(len(state)):
        for x in range(len(state[y])):
            if (x,y) in adjacent_coords:
                #find x,y in state modified and then swap it with hole. 
                location = state_modified.index(state[y][x])
                location2 = state_modified.index('*')
                state_modified[location], state_modified[location2] = state_modified[location2], state_modified[location]
                final_list.append((state[y][x],state_modified))   
                state_modified = copy.deepcopy(original)
    return final_list

'''
def ComputeNeighbors(state):
	return_val = []
	ZeroCoords = henrysdumbfunction(state)
	#check above 
	if int(ZeroCoords[0]) - 1 >= 0:
		return_val.append([int(ZeroCoords[0]) - 1, swap(state, ZeroCoords, tuple(str(int(ZeroCoords[0]) - 1), ZeroCoords[1]))])
	#below
	if int(ZeroCoords[0]) + 1 <= len(state) -1:
		return_val.append([int(ZeroCoords[0]) + 1, swap(state, ZeroCoords, tuple(str(int(ZeroCoords[0]) + 1), ZeroCoords[1]))])
	#left
	if int(ZeroCoords[1]) - 1 >= 0:
		return
	#right
	if int(ZeroCoords[1]) + 1 <= len(state) -1:
	#HELPHELPHELPHELPHELPHELPHELPHELPHELPHELPHELPHELPHELPHELPHELPHELP

	return tuple(return_val)
'''


DebugPrint(LoadFromFile("testcase.txt"))
