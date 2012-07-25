#It is an implementation of depth first search

class node:
    def __init__(self):
    	self.children=dict()
    	self.element=0



def find_element(element_to_find, stack):
    if  len(stack) < 1:
        return ""
    ptr=stack.pop();
    if ptr.element==element_to_find:
        return ptr
    else:      
    	for i in ptr.children:
            child=ptr.children[i]
	    stack.append(child)
    return find_element(element_to_find, stack)


#code below is for initiliazing the tree for bfs search
stack=list()
root= node()
root.children[1]=node()
root.children[1].element=1
root.children[2]=node()
root.children[2].element=2
root.children[1].children[1]=node()
root.children[1].children[1].element=3
stack.append(root)
a= find_element(3, stack)
if a:
    print a.element 
else:
    print "not found"    
