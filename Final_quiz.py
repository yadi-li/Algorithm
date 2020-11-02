#Algorithm: Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming
#Final quiz: Problem 10
#optimal binary search tree problem


#initialize a matrix to store the results of subproblems
n=7 
A = [[float("inf") for i in range(n)] for j in range(n)]

#frequencies of each item
pro_list=[0.2,0.05,0.17,0.1,0.2,0.03,0.25]


#s+1 is the length in the current problem, s starts from 0
for s in range(n):
	#i+s is the final position 
	for i in range(1,n-s+1):
		#pick a node as the dividing point, divide into two subtrees, iterate to find the min
		for r in range(i,i+s+1):
			#if the left subtree is empty
			if i>r-1: 
				#if the right subtree is empy
				if r+1>i+s:
					A[i-1][i+s-1]=min(sum(pro_list[i-1:i+s]),A[i-1][i+s-1])
				else:
					A[i-1][i+s-1]=min(sum(pro_list[i-1:i+s])+A[r][i+s-1],A[i-1][i+s-1])		
			elif r+1>i+s:
				A[i-1][i+s-1]=min(sum(pro_list[i-1:i+s])+A[i-1][r-2],A[i-1][i+s-1])
			else:
				A[i-1][i+s-1]=min(sum(pro_list[i-1:i+s])+A[i-1][r-2]+A[r][i+s-1],A[i-1][i+s-1])
			
#final solution: 2.23		
print(A[0][n-1])		



