#!/usr/local/bin/python

class prefix_tree:
    children={};
    count=0;
a=[]   
a.append(["a","b","c"]);
a.append(["d","e","f"]);
a.append(["a","b","c"]);
root=prefix_tree();

def insert(el,prev):
    if el not in prev.children:
        prev.children[el]= prefix_tree()
        next=prev.children[el]
        next.count+=1
        
    else:
        next=prev.children[el]
        next.count+=1
        
    return next

for i in range(0,3):
    prev=root
    for el in a[i]:
        print el
        prev=insert(el,prev)

print root.children["a"].count, root.children["a"].children["b"].count
print root.children["d"].count, root.children["d"].children["e"].count
        