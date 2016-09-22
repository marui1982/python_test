import sys,string
class mrpipe:
    v=None
    def __init__(self,v):
        self.v=1
    def v_to_s(self):
        #return str(self.v)
        print str(self.v)
    @classmethod
    def t1(self):
        return mrpipe(self.v)
    @property
    def t2(self):
        return mrpipe(self.v)
    @property
    def t3(self):
        return mrpipe(self.v)

mp=mrpipe(1)
mp.v_to_s()
mp.t1().t1().t1().t1().v_to_s()
mp.t2.t2.t2.v_to_s()

