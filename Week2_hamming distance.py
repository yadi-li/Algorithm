#Algorithm: Greedy Algorithms, Minimum Spanning Trees, and Dynamic Programming
#Week 2
#hamming distance

#input two integers n1 and n2
#return hamming distance
def hammingDistance(n1, n2) : 
    #XOR operation (bitwise comparison between binary representations of two integers)
    #Sets each bit to 1 if only one of two bits is 1
    x = n1 ^ n2  
    setBits = 0
  
    while (x > 0) : 
		#if the last bit is 1, the result of x & 1 is 1; otherwise, it is 0
		#count the number of 1s in XOR result (number of different bits in two integers)
        setBits += x & 1
        #right shift one position (add 0 at the beginning)
        x >>= 1
      
    return setBits  
  
print(hammingDistance(9, 14)) 


#convert integer to binary string
print("{0:b}".format(9))
print("{0:b}".format(14))
#convert binary string to integer
print(int("1001",2))



#create bit masks for hamming distance of 1
#number of bits=5
A=[1 << i for i in range(5)]
print(A)
#A=[1,2,4,8,16]

'''
print("{0:b}".format(2))
print("{0:b}".format(4))
print("{0:b}".format(8))
print("{0:b}".format(16))
'''


#example
#x=21
x=int("10101",2)
print(x)


#integers that have hamming distance of 1 from x
result=[]
for item in A:
	result.append(x^item)
print(result)


#create bit masks for hamming distance of 2
B=[]
for i in range(len(A)):
	for j in range(i+1,len(A)):
		B.append(A[i]^A[j])
print(B)


#integers that have hamming distance of 2 from x
result2=[]
for item in B:
	result2.append(x^item)
print(result2)







