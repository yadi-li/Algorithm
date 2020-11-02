#Algorithm: Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming
#Week 1
#Greedy algorithm

#Problem 1
#schedule jobs in decreasing order of the difference (weight - length)

#read the data
file = open("D:\\algorithm dataset\\jobs.txt", "r") 
data = file.readlines()

#10000 jobs
jobs=[[] for i in range(10000)]
i=0
for line in data[1:]:
	items=line.split()
	#weight of each job
	jobs[i].append(int(items[0]))
	#length of each job
	jobs[i].append(int(items[1]))
	#difference (weight-length) of each job
	jobs[i].append(jobs[i][0]-jobs[i][1])
	i+=1

#order the jobs by decreasing order of difference
#if two jobs have equal difference, schedule the job with higher weight first
order=sorted(range(len(jobs)),key=lambda k: (jobs[k][2], jobs[k][0]),reverse=True)


completion_time=[]
ordered_weight=[]
c=0
weighted_sum=0
#in the order of jobs in the schedule
for i in range(10000):
	length=jobs[order[i]][1]
	c+=length
	completion_time.append(c)
	ordered_weight.append(jobs[order[i]][0])
	weighted_sum+=completion_time[i]*ordered_weight[i]

	
	
#print(weighted_sum)
#answer: 69119377652


####################
#Problem 2
#schedule jobs in decreasing order of the ratio (weight/length)


#10000 jobs
jobs2=[[] for i in range(10000)]
i=0
for line in data[1:]:
	items=line.split()
	#weight of each job
	jobs2[i].append(int(items[0]))
	#length of each job
	jobs2[i].append(int(items[1]))
	#ratio (weight/length) of each job
	jobs2[i].append(jobs2[i][0]/jobs2[i][1])
	i+=1

#order the jobs by decreasing order of ratio
order2=sorted(range(len(jobs2)),key=lambda k: (jobs2[k][2]),reverse=True)


completion_time2=[]
ordered_weight2=[]
c2=0
weighted_sum2=0
#in the order of jobs in the schedule
for i in range(10000):
	length=jobs[order2[i]][1]
	c2+=length
	completion_time2.append(c2)
	ordered_weight2.append(jobs2[order2[i]][0])
	weighted_sum2+=completion_time2[i]*ordered_weight2[i]

	
#print(weighted_sum2)
#answer: 67311454237



#Problem 3
#Prim's minimum spanning tree

#read the data
file = open("D:\\algorithm dataset\\edges.txt", "r") 
data = file.readlines()

graph={}
for line in data[1:]:
	items=line.split()
	if int(items[0]) not in graph:
		graph[int(items[0])]={}
	#for each start_node, initialize a dictionary to store the edge cost
	graph[int(items[0])][int(items[1])]=int(items[2])
	
	#another direction
	if int(items[1]) not in graph:
		graph[int(items[1])]={}
	graph[int(items[1])][int(items[0])]=int(items[2])
		


#initialize the first node (randomly choose one node)
#X stores the nodes that have already been spanned
X=[1]
cost=0

#number of nodes in the graph: 500
while len(X)<500:
	min_cost=float('inf')
	next_node=0
	for start_node in X:
		#for each edge of each node in X
		for end_node in graph[start_node].keys():
			#if it is a cross edge, keep track of the minimum edge cost
			if end_node not in X and graph[start_node][end_node]<min_cost:
				min_cost=graph[start_node][end_node]
				next_node=end_node
	#append the node into X
	X.append(next_node)
	#accumulate the cost of MST
	cost+=min_cost

print(cost)
#answer: -3612829












