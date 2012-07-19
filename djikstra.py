
def find_min_dist_element(d,v,s):
    min=1000000
    for i in v:
        if d[i]<=min and i!=s:
            min=d[i]
            pos=i
    return pos
	

def djikstra(g,s,V):
    d={}
    p={}
    for i in V:
        d[i]=100000
    d[s]=0
    for j in g[s]:
        d[j]=g[s][j]

    q=list(V)
    q.remove(s)
    while len(q)!=0:
        u=find_min_dist_element(d,q,s)
        q.remove(u)
        for v in V:
            if  g.has_key(u) and g[u].has_key(v) and g[u][v]<100000: 
	        alt= d[u]+ g[u][v]
                if alt<d[v]:
                    d[v]=alt
                    p[v]= u
        
        
    return d


g={}
g[1]={2:3,3:100000}
g[2]={3:5,4:4}
v=[1,2,3,4]
s=1

djik=djikstra(g,s,v);
# print the distance array with distance b/w diff. nodes from source node:s
print djik
