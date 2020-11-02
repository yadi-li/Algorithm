#Algorithm: Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming
#Week 4
#knapsack problem

#Problem 1

#read the data
file = open("D:\\algorithm dataset\\knapsack1.txt", "r") 
data = file.readlines()

#knapsack size: 10000
#number of items: 100
W=int(data[0].split()[0])
n=int(data[0].split()[1])


#store the value and weight of each item in the dictionary
items={}
for i in range(1,len(data)):
	value=int(data[i].split()[0])
	weight=int(data[i].split()[1])
	items[i]=[value,weight]


#create a matrix to store the values
#number of rows: number of items+1
#number of columns: knapsack size+1
rows, cols = (n+1, W+1) 
matrix = [[0 for i in range(cols)] for j in range(rows)]

#when no item is in the knapsack, value=0
for i in range(cols):
	matrix[0][i]=0
#when weight=0, value=0
for j in range(rows):
	matrix[j][0]=0

for j in range(1,rows):
	#value of the current item:
	item_value=items[j][0]
	#weight of the current item:
	item_weight=items[j][1]
	
	for i in range(1, cols):	
		#if the current item is not in the knapsack
		value1=matrix[j-1][i]
		#if the current item is in the knapsack
		value2=matrix[j-1][i-item_weight]+item_value
	
		if item_weight<=i:
			matrix[j][i]=max(value1,value2)
		#else if weight of the current item is less than the current size
		else:
			matrix[j][i]=value1

#the maximum total value: 2493893
print(matrix[n][W])



#############
#Problem 2: big knapsack problem
#recursive solution

#increase recursion limit
import sys
sys.setrecursionlimit(3000)

#read the data
file = open("D:\\algorithm dataset\\knapsack_big.txt", "r") 
data = file.readlines()

#knapsack size: 2000000
#number of items: 2000
W=int(data[0].split()[0])
n=int(data[0].split()[1])


#store the value and weight of each item in the dictionary
items={}
for i in range(1,len(data)):
	value=int(data[i].split()[0])
	weight=int(data[i].split()[1])
	items[i]=[value,weight]


#i: item
#j: weight
#create a dictionary to store the results of subproblems
result_dic={}

def solve(i,j):
	if i==0 or j==0:
		result=0	
	else:
		#if current item is not in the knapsack			
		if (str(i-1),str(j)) not in result_dic:
			#recursive call
			value1=solve(i-1,j)
			#add into dictionary
			result_dic[(str(i-1),str(j))]=value1
		#else if it has been calculated
		else:
			value1=result_dic[(str(i-1),str(j))]
			
		#value of the current item:
		item_value=items[i][0]
		#weight of the current item:
		item_weight=items[i][1]
	
		#if the current item's weight is larger than the current weight, then the item can't be in the knapsack
		if item_weight>j:
			result=value1
		else: 
			#if current item is in the knapsack			
			if (str(i-1),str(j-item_weight)) not in result_dic:
				value2=solve(i-1,j-item_weight)
				result_dic[(str(i-1),str(j-item_weight))]=value2
				value2=value2+item_value
			else:
				value2=result_dic[(str(i-1),str(j-item_weight))]+item_value
			#select the maximum of value1 and value2	
			result=max(value1,value2)
		
	return result



print(solve(2000,2000000))
#answer: 4243395

