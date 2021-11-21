from sys import stdin

def inp():
	return stdin.readline().rstrip()

def iinp():
	return int(inp())

def mp():
	return map(int, inp().split())

def liinp():
	return list(mp())


def max_profit(prices):
	max_profit  = -float('inf')
	buy			= prices[0]

	for i in range(1, len(prices)):
		profit = prices[i]-buy
		if profit > max_profit:
			max_profit = profit
		if prices[i] < buy:
			buy = prices[i]

	return max_profit if max_profit>0 else 0

if __name__ == "__main__":

	prices = liinp()
	print(max_profit(prices))