#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 02:39:32 2019

@author: rushit
"""
"Chpt1 - Strings & Arrays"

"Q1.1: Implement an algorihm to determine if a string has all unique characters"

def string_unique_chars(string):
    if len(string) is not 0:
        l = len(string)
        char_keeper = {}
        
        for elem in string:
            if elem in char_keeper:
                return False
            else:
                char_keeper[elem]=1
                
        return True
    else:
        print("Please enter a valid string")

"Q1.2: Write code to reverse a C-Syle String. (C-String means that ""abcd"" is" 
"represenented as five characters, including the null character.)"

def reverse_c_string(string):
    if len(string) is not 0:
        ind = 0
        elem = string[ind]
        temp = []
        NULL_CHAR = '\\'
        while elem is not NULL_CHAR:
            temp.append(elem)
            ind += 1
            elem = string[ind]
        
        string_rev = ""
        for _ in range(len(temp)):
            string_rev+=temp.pop()
            
        print(string_rev)
        return string_rev
    else:
        print("Please enter a valid string")
