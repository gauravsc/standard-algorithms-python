v=[3,4,5,6]
w=[4,6,7,10]
W=15
length=len(v)
t=[[0]*(W+1)]*(length+1)
for i in range(1, length+1):
    for j in range(0,W+1):
        if j>=w[i-1]:
	    t[i][j]=max(t[i][j-w[i-1]]+v[i-1],t[i-1][j])
        else:
	    t[i][j]=t[i-1][j]

print t[length][W]
