# -*- coding: utf8 -*-  
#字符串相似度算法  
#!/usr/bin/env python  
__author__ = 'Administrator'  

"""  
def levenshtein(a,b):  
    "Calculates the Levenshtein distance between a and b."  
    n, m = len(a), len(b)  
    if n > m:  
        # Make sure n <= m, to use O(min(n,m)) space  
        a,b = b,a  
        n,m = m,n  
    current = range(n+1)  
    for i in range(1,m+1):  
        previous, current = current, [i]+[0]*n  
        for j in range(1,n+1):  
            add, delete = previous[j]+1, current[j-1]+1  
            change = previous[j-1]  
            if a[j-1] != b[i-1]:  
                change = change + 1  
            current[j] = min(add, delete, change)  
    return current[n]  
"""
  
def levenshtein_distance(first, second):  
    """Find the Levenshtein distance between two strings."""  
    if len(first) > len(second):  
        first, second = second, first  
    if len(second) == 0:  
        return len(first)  
    first_length = len(first) + 1  
    second_length = len(second) + 1  
    distance_matrix = [range(second_length) for x in range(first_length)]  
    for i in range(1, first_length):  
        for j in range(1, second_length):  
            deletion = distance_matrix[i-1][j] + 1  
            insertion = distance_matrix[i][j-1] + 1  
            substitution = distance_matrix[i-1][j-1]  
            if first[i-1] != second[j-1]:  
                substitution += 1  
            distance_matrix[i][j] = min(insertion, deletion, substitution)  
    return distance_matrix[first_length-1][second_length-1]  


def list2str(r,sep="\t"):
    for j in range(0,r.__len__()):
        r[j]=str(r[j])
    return sep.join(r)

def address_specity_level(address):
    frequently_used_character=['区','村','镇','路','县','街','单元','楼','城','栋','组','道','室','巷','里','弄','旗','乡','庄','塘',
        '社','幢','园','场','号']
    c=0
    res=[]
    for i in frequently_used_character:
        if i in address:
            c+=1
            res.append(i)
    print c,list2str(res)

#print levenshtein_distance('中国','yz中国北京')
print address_specity_level('北京市海淀区中关村东路105号院6号楼603')
