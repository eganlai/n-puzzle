


def LoadFromFile(filepath):
	henrys_list = []
	n = 0
	with open(filepath, 'r') as f:
		count = 0
		for line in f:
			line_list = []
			if count == 0:
				n = f
			else:
				dog = line.split("\t")
				for item in dog:
					if item == "*":
						dog[item] = 0
					else:
						dog[item] = int(dog[item])
				henrys_list.append(line_list)
			count+=1
	return henrys_list

		


def DebugPrint(teerons_list):
	for i in teerons_list:
		funny_dog_really_funny = ""
		for j in i:
			funny_dog_really_funny += j + "\t"
		print(funny_dog_really_funny)



DebugPrint(LoadFromFile("testcase.txt"))
