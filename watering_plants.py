from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())


def watering_plants(plants, capacity):
	step = 0
	cap  = capacity
	
	for i, val in enumerate(plants):
		if cap-val<0:
			cap   = capacity
			cap  -= val
			step += i*2+1 # return to the beginning of the array 2*i at the river +1
			continue
		step += 1
		cap  -= val

	return step

if __name__=="__main__":
	plants   = [7,7,7,7,7,7,7]
	capacity = 8
	print(watering_plants(plants, capacity))