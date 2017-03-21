#!/usr/bin/env python
# encoding: utf-8
import random
def get_n_random_num(n):
    res=[]
    for i in range(0,n):
        res.append(random.random())
    return res

def calulate_possibility(ll,v):
    tt=len(ll)
    c=0
    if tt==0:return 0
    for l in ll:
        if l<v:
            c+=1
    return c*1.0/tt

def experiment(random_num=5,default_prosibility=0.5,run_times=1000):
    res=[]
    for i in range(0,run_times):
        ll=get_n_random_num(random_num)
        p=calulate_possibility(ll,default_prosibility)
        #res.append(p-default_prosibility)
        res.append(p)
    #avg=sum(res)*1.0/len(res)
    #print sum(res),len(res),avg
    #return avg
    #print 'diff_avg=%s\trandom_num=%s,default_prosibility=%s,run_times=%s'%(avg,random_num,default_prosibility,run_times)
    return calculate_posibility_distribution(res,default_prosibility)
    #return res
def calculate_posibility_distribution(ll,default_prosibility):
    diff_tong={}
    for l in ll:
        #print l,l-default_prosibility,abs(l-default_prosibility)/default_prosibility
        diff=abs(l-default_prosibility)/default_prosibility
        diff_tong[int(diff/0.1)]=diff_tong.get(int(diff/0.1),0)+1
    #for d in diff_tong:
    #    print d,diff_tong[d]
    return diff_tong
        
#print random.random() 
if __name__=='__main__':
    """ 
        实验目的:数据量为n时,数据的可信程度
        实验设计:
            设特征的实际概率为default_prosibility
            计算n个采样时的偏差：如有n个采样(n条数据)，根据其计算概率(其概率可能与实际存在差异)
                取n个随机数(0,1)：其效率default_prosibility则认为结果命中
            计算偏差的概率分布(离散型的表示)
    """
    run_num=10000
    default_prosibility=0.30
    for i in [1,5,10,20]:
        diff_tong=experiment(i,default_prosibility,run_num)
        for d in diff_tong:
            print i,d,diff_tong[d]
    
