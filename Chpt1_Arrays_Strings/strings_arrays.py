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



"Q1.3: Write a method to replace all spaces in a string with '%20: You may 
"assume that the string has sufficient space at the end to hold the additional 
"characters, and that you are given the 'true' length of the string."

def URLify(sstring, len_s):
    s_final=[]
    for char in string:
        if char is not ' ':
            s_final.append(char)
        else:
            s_final.append('%20')
    s_returned = ''.join(s_final)
    return s_returned

"Q1.4: Given a string, write a function to check if it is a permutation of a" 
"palindrome. A palindrome is a word or phrase that is the same forwards and" 
"backwards. A permutation is a rearrangement of letters.The palindrome does "
"not need to be limited to just dictionary words."

class MyDict:
    def __init__(self):
        self.dict = {}
        
    def add(self, element):            
        if element in self.dict.keys():
            self.dict[element]+=1
        else:
            self.dict[element]=1

def is_permutation_palindrome(string_orig):
    count = MyDict()
    string = string_orig.lower() #case insensitive
    for char in string:
        if char is not " ":     #space insensitive
            count.add(char)
    
    flag = False
    count_odd = 0
    for key in count.dict.keys():
        if count.dict[key]%2 is not 0:
            count_odd+=1
            
    if count_odd <= 1:
        flag = True
    
    return flag

            
"""Q1.5: One Away: There are three types of edits that can be performed on 
strings: insert a character, remove a character, or replace a character. Given 
two strings, write a function to check if they are one edit (or zero edits) 
away."""

def one_away(str1, str2):
    edit_dist = 0
    #base case len(str1 or str2 or both == 0)
    
    #base case len(str1)==len(str2)==1, = 1 edit
    
    #when string1 and sring 2 are same length
    n = len(str1)
    
    for i in range(n):
        n1 = len(str1) 
        n2 = len(str2)
        print(i)
        if str1[i] is not str2[i]:
            if n1>n2:
                str2 = str2[0:i]+str1[i]+str2[i:n2]
            elif n2>n1:
                str1 = str1[0:i]+str2[i]+str1[i:n1]
            edit_dist += 1
                
                
        
    
    #differentt lengths
    
    
    print(edit_dist)
    

"""Q1.5: String Compression: Implement a method to perform basic string 
compression using the counts of repeated characters. For example, 
the string aabcccccaaa would become a2b1c5a3. If the "compressed" string 
would not become smaller than the original string, your method should return 
the original string. You can assume the string has only uppercase and 
lowercase letters (a - z)."""

def string_compression(string):
    n = len(string)
    i = 0
    count=0
    final_str = ''
    
    while(i<n):
        char = string[i]
        while(string[i+1] is char):
            count += 1
            i+=1
            if i>n-2:
                break
    
        final_str = final_str + char + str(count)
        count = 1
        i+=1
        
    if len(final_str)>n:
        return string
    else:
        return final_str
    
"""Q1.6: Rotate Matrix: Given an image represented by an NxN matrix, where each 
pixel in the image is 4 bytes, write a method to rotate the image by 90 degrees. 
Can you do this in place?"""

            
