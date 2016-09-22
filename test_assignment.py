#!/usr/bin/env python
# encoding: utf-8
import copy
def assignment():
    def t(x):
        x+=[4]
        print x
    
    a=[1,2,3]
    b=a
    b+=[4]
    print a,b 
    print t(a)

assignment()    #测试赋值

def test_copy():
    class X():
        v=1 

    c='c'
    x=X()
    a=[1,2,3,c,x]
    b=copy.copy(a)
    b+=[4]
    print a,b
    c='d'
    print a,b,a[4].v,b[4].v

    x.v=2
    print a,b,a[4].v,b[4].v

test_copy()



