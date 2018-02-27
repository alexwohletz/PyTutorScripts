# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 06:33:34 2018

@author: awohl
"""


def flat(lst):
    '''take a list of any depth and recursively flatten it'''
    def flatten(l):
    
        flat = []
        for i in l:
        
            print(i)
            print(isinstance(i,list))
            if isinstance(i,list):
                for x in i:
                    flat.append(x)
            else:
                flat.append(i)
        return flat

    while any([isinstance(i,list) for i in lst]): #check if list is flat
 
        lst = flatten(lst)
    return lst

l = [2, 19, 10, ['a', 'b', ["nth",["ith"]]]]


import collections

def flatten(l):
    for el in l:
        if isinstance(el, collections.Iterable) and not isinstance(el, (str, bytes)):
            yield from flatten(el)
        else:
            yield el


#l = [2, 19, 10, ['a', 'b', ["nth",["ith"]]]]            
#to_dict(l) -->
            #{1: [2,19,10],
            # 2: ['a','b'],
            # 3: ['nth'],
            # 4: ['ith'],}
            