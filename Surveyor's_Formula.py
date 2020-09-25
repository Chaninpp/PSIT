def main():
	
	result_sum = 0
	num = int(input("Enter number of co-ordinates: "))
	lis = [tuple([int(j) for j in input("Enter x"+str(i+1)+", y"+str(i+1)+": ").split()]) for i in range(num)]
	print(lis)
	temp_1 = sum([lis[i][1]*lis[(i+1) if i+1 < num else 0][0] for i in range(num)])
	temp_2 = sum([lis[i][0]*lis[(i+1) if i+1 < num else 0][1] for i in range(num)])
	print("A =", (temp_1-temp_2)/2)

main()
