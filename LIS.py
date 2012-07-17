#!/usr/bin/env python
import sys
def binary_search(elements,x):
    end=len(elements)-1
    beg=0
    mid=(beg+end)/2
    while elements[mid] != x and beg<end:
        if(elements[mid]==x):
            return mid
        elif(elements[mid]<=x):
            beg=mid+1
        else:
            end=mid-1
        mid=(beg+end)/2
        
    return mid


def find_l(elements,x):
    mid=binary_search(elements,x)
    if(mid==0):
        return mid;
    if(elements[mid]<x):
        return mid
    elif(elements[mid]>x and elements[mid-1]<x):
        return mid-1
    elif(elements[mid]==x and elements[mid-1]<x):
        return mid-1
    else:
        return -1
    
def print_series(el,m,p,L):
    L=m[L]
    i=L
    while L>=0:
        print el[L],
        L=p[L]
        
def lis_maintain():
    lis=[sys.maxint for x in xrange(len(elements)+1)]
    lis[0]=-10000
    l=0
    m=[-1 for x in xrange (len(elements))]
    p=[-1 for x in xrange (len(elements))]
    for i in range(0,len(elements)):
        mid=find_l(lis,elements[i])
        p[i]=m[mid]
        if(elements[i]<lis[mid+1]):
            lis[mid+1]=elements[i]
            l=max(l,mid+1)
            m[mid+1]=i
    print_series(elements,m,p,l)
    
elements=[81,82,83,84,86,87,88,1,5,4,7,8,9,10,90]

lis_maintain();
