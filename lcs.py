x=["","a","b","e","f"]
y=["","a","c","f"]

lcs=[[0 for z in xrange(6)] for z in xrange(5)]

for i in range(1,len(x)):
    for j in range(1,len(y)):
        if(x[i]==y[j]):
	    lcs[i][j]=lcs[i-1][j-1]+1
        else:
	    lcs[i][j]= max(lcs[i-1][j],lcs[i][j-1])


print lcs



def backtrack(lcs,x,y,i,j):
    if i == 0 or j == 0:
        return ""
    elif x[i]==y[j]:
        return backtrack(lcs, x, y, i-1, j-1) + x[i]
    else:
        if lcs[i][j-1] > lcs[i-1][j]:
            return backtrack(lcs, x, y, i, j-1)
        else:
            return backtrack(lcs, x, y, i-1, j)

print backtrack(lcs,x,y,4,3)
