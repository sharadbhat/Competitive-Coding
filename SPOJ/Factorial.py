# SPOJ
# http://www.spoj.com/problems/FCTRL/

inputs = int(input())

for i in range(inputs):
	value = int(input())
	count = 0
	for i in range(1, 100):
		if 5**i > value:
			break
		else:
			count += value//(5 ** i)
	print(count)
