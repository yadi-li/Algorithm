#Algorithm: Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming
#Week 3
#Huffman code & dynamic programming


#Problem1
import math

#Heap functions
#bubble down
#for min heap, parent should be smaller than the children
#node begins with 0
def bubble_down_min(i,heap):
	minindex=i
	#left children
	l=2*i+1
	#right children
	r=2*i+2
	#if left child exist and left child is smaller than node i
	#update minindex
	if l<len(heap) and heap[l]<heap[minindex]:
		minindex=l
	if r<len(heap) and heap[r]<heap[minindex]:
		minindex=r
	#if left or right child is smaller than node i
	if minindex!=i:
		heap[i],heap[minindex]=heap[minindex],heap[i]
		#recursively call bubble_down_min
		bubble_down_min(minindex,heap)
	return heap
	
	
	
#bubble up
#for min heap, parent should be smaller than the children
#node begins with 0
def bubble_up_min(i,heap):
	if i%2==0:
		parent=int(i/2-1)
	else:
		parent=math.floor(i/2)
	#if parent exists and is larger than node i
	if parent>=0 and heap[parent]>heap[i]:
		heap[i],heap[parent]=heap[parent],heap[i]
		#recursively call bubble_up_min
		bubble_up_min(parent,heap)
	return heap	
	
#extract min
def extract_min(heap):
	min_key=heap[0]
	#switch with the last element in heap
	heap[0],heap[-1]=heap[-1],heap[0]
	del heap[-1]
	bubble_down_min(0,heap)
	return min_key
	
#insert
#for min heap
def insert_min(key,heap):
	heap.append(key)
	i=len(heap)-1
	bubble_up_min(i,heap)
	return heap
	

#read the data
file = open("D:\\algorithm dataset\\huffman.txt", "r") 
data = file.readlines()

#create heap
heap=[]
#create dictionary
node={}

for i in range(1,len(data)):
	#insert the weights into the heap
	insert_min(int(data[i]),heap)
	#insert weight and node ID into dictionary
	node[int(data[i])]=i



result=[]
#1000 nodes, 999 mergers
for i in range(999):
	#extract two smallest weights
	node1=extract_min(heap)
	node2=extract_min(heap)
	#find the index of these two nodes
	index1=node[node1]
	index2=node[node2]
	#add into result list
	#if there is only one index for the weight (an original node)
	if type(index1) is int:
		result.append(index1)
	#else if it is a list of indices
	else: 
		result.extend(index1)
	if type(index2) is int:
		result.append(index2)
	else:
		result.extend(index2)
	#calculate new weight (node1+node2)
	new_weight=node1+node2
	#insert into heap
	insert_min(new_weight,heap)
	#add into the dictionary
	node[new_weight]=[]
	if type(index1) is int:
		node[new_weight].append(index1)
	else: 
		node[new_weight].extend(index1)
	if type(index2) is int:
		node[new_weight].append(index2)
	else:
		node[new_weight].extend(index2)
	


import collections
#count the number of mergers for each node (the length of code)
counter=collections.Counter(result)
#print(counter)
#the maximum length of a codeword in the resulting Huffman code: 19
print(counter.most_common()[0][1])
#the minimum length of a codeword in the resulting Huffman code: 9
print(counter.most_common()[-1][1])






#Problem2
#maximum-weight independent set of a path graph
#dynamic programming

#read the data
file = open("D:\\algorithm dataset\\mwis.txt", "r") 
data = file.readlines()

#creat array to store the weight of each node
weight=[]
for i in range(len(data)):
	#node index starts with 1
	weight.append(int(data[i]))

#create array to store the solution 
A=[[] for i in range(1001)]

#base case
A[0]=0
A[1]=weight[1]

#recursive solution
for i in range(2,1001):
	A[i]=max(A[i-1],A[i-2]+weight[i])
	

#reconstruction
result=[]
while i>0:
	#if node i is not in the final solution
	if A[i-1]>=A[i-2]+weight[i]:
		i=i-1
	else:
		#node i is in the final solution
		result.append(i)
		i=i-2
		

binary_result=[]
#check if these nodes are in the solution
for i in [1, 2, 3, 4, 17, 117, 517, 997]:
	if i in result:
		binary_result.append(1)
	else:
		binary_result.append(0)
		
print(binary_result)
#answer: 10100110
