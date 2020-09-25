a = input()
result = 0
nub = 0
while a != '300':
	if int(a) and a != '0':
		result += float(a)
		nub += 1
	else:
		pass
	a = input()
print(result, '/',nub,'=','\n')
print(result/nub)