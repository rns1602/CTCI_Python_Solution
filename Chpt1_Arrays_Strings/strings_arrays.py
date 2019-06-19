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

"Q1.2: Design an algorithm and write code to remove the duplicate characters in" 
"a string without using any additional buffer NOTE: One or two additional" 
"variables are fine An extra copy of the array is not."

class CharCarrier():
    
    def __init__(self,ind,char):
        self.index = ind
        self.value = ord(char)
        self.dupe = False
        return
        
    def get_char(self):
        return chr(self.value)

def merge_sort(arr):
    "https://www.geeksforgeeks.org/merge-sort/"
    if len(arr) >1: 
        mid = len(arr)//2 #Finding the mid of the array 
        L = arr[:mid] # Dividing the array elements  
        R = arr[mid:] # into 2 halves 
  
        merge_sort(L) # Sorting the first half 
        merge_sort(R) # Sorting the second half 
  
        i = j = k = 0
          
        # Copy data to temp arrays L[] and R[] 
        while i < len(L) and j < len(R): 
            if L[i].value < R[j].value: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1

        # Checking if any element was left 
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1

def remove_duplicates_string(string):
    
    string_new = []
    
    for i in range(len(string)):
        s = CharCarrier(i, string[i])
        string_new.append(s)

    merge_sort(string_new)
    
    string_final = []
    string_final.append(chr(string_new[0].value))
    for i in range(len(string_new)-1):
        if string_new[i].value is not string_new[i+1].value:
            string_final.append(chr(string_new[i+1].value))
    
    return string_final
        
x = remove_duplicates_string("mayank")
for i in range(len(x)):
    print(x[i])
