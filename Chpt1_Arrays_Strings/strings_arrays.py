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

"Q1.2 (4th edition): Write code to reverse a C-Syle String. (C-String means that ""abcd"" is" 
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

"Q1.2 : Check Permutation: Given two strings, write a method to decide if one"
"       is a permutation of the other."

#Methtod 1
def string_to_ascii(string):
    ascii_string = []
    for char in string:
        ascii_string.append(ord(char))
    return ascii_string

def strings_permutation1(string1, string2):
    if len(string1)!=0 and len(string2)!=0:
        if len(string1)!=len(string2):
            return False
        else:
            s1 = string_to_ascii(string1)
            s2 = string_to_ascii(string2)
            
            sum1=0;sum2=0;prod1=1;prod2=1;
            
            for i in range(len(s1)):
                sum1 += s1[i]
                prod1 = prod1*s1[i]
                
            for i in range(len(s2)):
                sum2 += s2[i]
                prod2 = prod2*s2[i]
            
            if sum1==sum2 and prod1==prod2:
                return True
            else:
                return [False,s1,s2]
    else:
        return None
    
#Method 2
def string_to_dict(string):
    dict_of_string = {}
    for char_key in string:
        if dict_of_string.get(char_key,0) is 0:
            dict_of_string[char_key] = 1
        else:
            dict_of_string[char_key] += 1 
        
    return dict_of_string

def strings_permutation2(string1, string2):
    if len(string1)!=0 and len(string2)!=0:
        if len(string1)==len(string2):
            dict1 = string_to_dict(string1)
            dict2 = string_to_dict(string2)
            
            if len(list(dict1.keys()))==len(list(dict2.keys())):
                for key in list(dict1.keys()):
                    if key in list(dict2.keys()):
                        if dict1[key]!=dict2[key]:
                            return False
                        else:
                            continue
                    else:
                        return False
            else:
                return False
        else:
            return False
    else:
        return None
    
    return True

"Q1.3 (4th edition): Design an algorithm and write code to remove the duplicate 
"characters in a string without using any additional buffer NOTE: One or two "
"additional variables are fine An extra copy of the array is not." 

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

