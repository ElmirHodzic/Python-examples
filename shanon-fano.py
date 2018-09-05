#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Elmir Hodzic
"""

import operator

recenica  = "Algorithm of Shannon - Fanovog coding implementation.";


def built_dict(s):
    dictionary = {};
    
    for i in range(len(s)):
        if recenica[i] in dictionary:
            dictionary[s[i]] += 1;
        else:
            dictionary[s[i]] = 1;
    
    return dictionary;

def sort_dict(d):
    sorted_dict = sorted(d.items(), key=operator.itemgetter(1), reverse = True);
    return sorted_dict;

def initialize_list_of_codes(s):
    l = {};
    for i in range(len(s)):
        l[s[i][0]] = '';
    return l;
    
def sum_list_toupples(l, a, b):
    sum = 0
    for i in range(a, b):
        sum += l[i][1];
    return sum;

def divide_list(l, start, end):
    for i in range(1, end - start):
        if sum_list_toupples(l, start, start + i)  >= sum_list_toupples(l, start + i, end):
            return start + i
    return -1;

def one_list_to_two(l, index):
    l1 = [];
    l2 = [];
    
    for i in range(0, index):
        l1.append(l[i]);
        
    for i in range(index, len(l)):
        l2.append(l[i]);
        
    return l1, l2;

def add_binary(dictionary,l, c):
    for i in range(len(l)):
        dictionary[l[i][0]] += c;

def make_shannon_codes(l, list_of_codes):    
    left = [];
    right = [];
    (left, right) = one_list_to_two(l, divide_list(l, 0, len(l)));    
    add_binary(list_of_codes, left, '0');    
    add_binary(list_of_codes, right, '1');    
    print(left, right)    
    if len(right) > 1: 
        make_shannon_codes(right, list_of_codes);    

    if len(left) > 1: 
        make_shannon_codes(left, list_of_codes);
        

def ShannonFano(string):
    d = built_dict(string)
    sorted_dict = sort_dict(d)
    list_of_codes = initialize_list_of_codes(sorted_dict)
    make_shannon_codes(sorted_dict, list_of_codes)
    for i in range(len(sorted_dict)):
        print(sorted_dict[i][0] ,list_of_codes[sorted_dict[i][0]], sorted_dict[i][1]);

ShannonFano(recenica);
