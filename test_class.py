#!/usr/bin/env python
# encoding: utf-8
import sys,string
class A1:
    def a1(self):
        print 'use A1 a1'
    def a3(self):
        print 'user A1 a3'

class A2(A1):
    def a1(self):
        print 'use A2 a1'
    def a2(self):
        print 'user A2 a2'

def test_inherit():
    print '继承======================='
    a=A1()
    a.a1()
    a.a3()

    print '==============='
    b=A2()
    b.a1()
    b.a2()
    b.a3()
