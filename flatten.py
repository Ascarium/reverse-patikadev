# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 16:24:46 2022

@author: Özgür Nazlı
"""

input1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]

output1=[]
def flatten(x):
    for i in x:
        if  isinstance(i,list):
            flatten(i)
        else:
            output1.append(i)
    return output1
print(flatten(input1))