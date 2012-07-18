
#knapsack 0-1 DP solution algorithm with condition: each element can be used atmost once 
v=[3,4,5,6]
w=[4,6,7,10]
W=15
length=len(v)
t=[[0]*(W+1)]*(length+1)
for i in range(1, length+1):
    temp_record={}
    for j in range(0,W+1):
        temp_record[j]=[]
    for j in range(0,W+1):
        if j>=w[i-1]:
	    if(t[i][j-w[i-1]]+v[i-1]>t[i-1][j] and i-1 not in temp_record[j-w[i-1]]):
	        temp_record[j].append(i-1)
	        t[i][j]=max(t[i][j-w[i-1]]+v[i-1],t[i-1][j])
        else:
	    t[i][j]=t[i-1][j]

print t[length][W]
