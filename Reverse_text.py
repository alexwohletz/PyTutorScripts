# -*- coding: utf-8 -*-
"""
Created on Tue Feb 20 17:23:02 2018

@author: awohl
"""

def strReverseI(s):
    '''
    (str) -> str

    A function that reverses the process of strReverseR(s),
    which means the reversed string in user input into its original state
    
    >>>strReverseR("drah si ssalc siht")
    this class is hard
    >>>strReverseR("evisrucer dnatsrednu t'nod llits I sseug I")
    I guess I still don't understand recursive
    >>>strReverseR("yadot erom yranib dnatsrednu I sseug I")
    I guess I understand binary more today

    '''
    rstr = ''
    for ch in s:
        rstr = ch + rstr

    return rstr

def strReverseR(s):
    '''
    (str) -> str

    A function that reverses the string in user input using
    the algorithm of recursive function

    >>>strReverseR("this class is hard")
    drah si ssalc siht
    >>>strReverseR("I guess I still don't understand recursive")
    evisrucer dnatsrednu t'nod llits I sseug I
    >>>strReverseR("I guess I understand binary more today")
    yadot erom yranib dnatsrednu I sseug I

    '''
    if (len(s) == 1) or (len(s) == 0):
        return s
    else:
        return strReverseR(s[1:]) + s[0]

def test_reverse(f): ###This is the clue
    '''
    (str) -> str

    A function that checks if testcases to functions strReverseR
    and strReverseI are correct or error and prints the following
    results on Python
    
    >>>Checking strReverseR('testing123')...
    its value '321gnitset' is correct!
    >>>Checking strReverseI('a')...
    Error: has wrong value 'a', expected 'b'.
    '''
    test_cases = [
     ('', ''),
     ('a', 'a'),
     ('aaaa', 'aaaa'),
     ('abc', 'cba'),
     ('hello', 'olleh'),
     ('racecar', 'racecar'),
     ('testing123', '321gnitset'),
     ('#CIS 210', '012 SIC#'),
     ('a', 'b')
                 ]

    for test_case in test_cases:
        
        print("Checking {}('{}')".format(f.__name__,test_case[0]))
        if f(test_case[0]) == test_case[1]:
            print( "its value '{}' is correct!".format(test_case[1]))
        else:
            print( "Error: has wrong value '{}', expected '{}'".format(test_case[0], test_case[1]))
    

