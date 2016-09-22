import os
import sys

class test_4_define_sequence():
    
    @classmethod
    def run1(self):
        self.f1()
        self.f2()

    def f1(self):
        print 'f1'

    def f2(self):
        print 'f2'

    @classmethod
    def run2():
        self.f1()
        self.f2()

#test_4_define_sequence.run1()
#test_4_define_sequence.run2()
def f(a):
    print a 
f(None)

#函数的变长参数===============================
def funcD(a, b, *c):
  print a
  print b
  print "length of c is: %d " % len(c)
  print c
funcD(1,2,3,4,5,6,7,8,9)
