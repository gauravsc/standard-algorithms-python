from collections import deque

class node:
    def __init__(self):
    	self.children=dict()
    	self.element=0



def find_element(element_to_find, queue):
    if  len(queue) < 1:
        return ""
    ptr=queue.popleft();
    if ptr.element==element_to_find:
        return ptr
    else:      
    	for i in ptr.children:
            child=ptr.children[i]
	    queue.append(child)
    return find_element(element_to_find, queue)


#code below is for initiliazing the tree for bfs search
queue=deque()
root= node()
root.children[1]=node()
root.children[1].element=1
root.children[2]=node()
root.children[2].element=2
root.children[1].children[1]=node()
root.children[1].children[1].element=3
queue.append(root)
a= find_element(6, queue)
if a:
    print a.element 
else:
    print "not found"    
