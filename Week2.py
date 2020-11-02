#Algorithm: Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming
#Week 2
#Clustering algorithm


#Problem1
#read the data
file = open("D:\\algorithm dataset\\clustering1.txt", "r") 
data = file.readlines()

#create a list for edges
edges=[[] for i in range(len(data)-1)]
for i in range(1,len(data)):
	items=data[i].split()
	#head of the edge
	edges[i-1].append(int(items[0]))
	#tail of the edge
	edges[i-1].append(int(items[1]))
	#distance of the edge
	edges[i-1].append(int(items[2]))


#sort edges based on distance (from smallest to largest)
sorted_edges=sorted(edges, key = lambda x: int(x[2]))


#initialize an array for parent pointers (every node points to itself at the beginning)
#number of nodes:500
parent=list(range(1,501))

#initalize rank to be 0 for all nodes
rank=[0]*500

#function of finding the leader of each cluster
def find(x):
	while parent[x-1]!=x:
		x=parent[x-1]
	return x



#500 clusters at the beginning (each node is a cluster)
k=500
i=0
#stop when there are 4 clusters left
while k>4:
	#traverse all edges (from smallest to largest distance)
	edge=sorted_edges[i]
	head=edge[0]
	tail=edge[1]
	leader1=find(head)
	leader2=find(tail)
	#if two nodes are in different clusters
	if leader1!=leader2:
		#union the two clusters
		#number of clusters decrease by 1
		k=k-1
		#union by rank
		#if leader1 has higher rank, then set leader2's parent to be leader1
		if rank[leader1-1]>rank[leader2-1]:
			parent[leader2-1]=leader1
		else:
			parent[leader1-1]=leader2
			#update rank if two leaders have the same rank
			if rank[leader1-1]==rank[leader2-1]:
				rank[leader2-1]+=1
	i=i+1

#find the next edge that crosses two clusters
while True:
	next_edge=sorted_edges[i]
	head=next_edge[0]
	tail=next_edge[1]
	leader1=find(head)
	leader2=find(tail)
	#if two nodes are in different clusters
	if leader1!=leader2:
		max_spacing=next_edge[2]
		break
	i=i+1
	
	
print(max_spacing)
#answer: 106	






#################################
#Problem2
#distance is defined as Hamming distance

#read the data
file = open("D:\\algorithm dataset\\clustering_big.txt", "r") 
data = file.readlines()


#initialize array to store the parent pointers
#number of nodes: 200000
parent=list(range(1,200001))
#initialize array to store ranks
rank=[0]*200000

#function of finding the leader of each cluster
def find(x):
	while parent[x-1]!=x:
		x=parent[x-1]
	return x

#union function
def union(x,y):
	leader1=find(x)
	leader2=find(y)
	#if two nodes are in different clusters
	if leader1!=leader2:
		#union the two clusters
		#union by rank
		#if leader1 has higher rank, then set leader2's parent to be leader1
		if rank[leader1-1]>rank[leader2-1]:
			parent[leader2-1]=leader1
		else:
			parent[leader1-1]=leader2
			#update rank if two leaders have the same rank
			if rank[leader1-1]==rank[leader2-1]:
				rank[leader2-1]+=1

#initialize dictionary
node={}
for i in range(1,len(data)):
	#remove space betwen 0 and 1
	data[i]=data[i].replace(" ", "")
	#convert bit string into integer
	node_int=int(data[i],2)
	
	if node_int in node:
		#if two nodes have the same integer, union them into one cluster
		union(node[node_int][0],i)
	else:
		node[node_int]=[]
	node[node_int].append(i)



#create bit masks for hamming distance of 1
#number of bits=24
A=[1 << i for i in range(24)]
#print(A)

#create bit masks for hamming distance of 2
B=[]
for i in range(len(A)):
	for j in range(i+1,len(A)):
		B.append(A[i]^A[j])
#print(len(B))

for key in node.keys():
	result=[]
	#integers that have hamming distance of 1 from x
	for item in A:
		result.append(key^item)
	#integers that have hamming distance of 2 from x
	for item in B:
		result.append(key^item)
	#check for each integer that has hamming distance<=2 and union the corresponding nodes
	for item in result:
		if item in node.keys():
			union(node[key][0],node[item][0])
	
			
#get the clusters for each node
clusters=[find(x) for x in range(1,200001)]
#remove duplicated values
clusters = list(dict.fromkeys(clusters))
#number of distinct clusters
print(len(clusters))
#answer:6118







