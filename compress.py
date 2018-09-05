#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Lempel Ziw Welch compressor python
@author: Elmir Hodzic
"""


imit = 2**16-1

def reset_dict(dictionary):
    dictionary.clear()
    dictionary["#"] = 0
    for i in range(1, 27):
        dictionary[chr(64 + i)] = i
        
def reset_list():
    dictionary = []
    dictionary.append("#")
    for i in range(1, 27):
        dictionary.append(chr(64 + i))
    return dictionary
        
def Encode(in_stream, out_stream):
    f = open(in_stream, 'r')    
    text = f.read()    
    text_out = open(out_stream, 'w')
    
    dictionary = {}
    reset_dict(dictionary)    
    line = ""
    
    while True:        
        if len(dictionary) == limit:
            reset_dict(dictionary)    
        
        simbol = text[0]        
        
        text = text[1:]
        line += simbol
        
        if dictionary.has_key(line) == False:            
            dictionary[line] = len(dictionary)
            line = line[:-1]
            #bytes_to_bits            
            text_out.write('{0:016b}'.format(dictionary[line]))
            line = simbol
        if simbol == '#':
            break;
    if len(line) != 0:
        #bytes_to_bits        
        text_out.write('{0:016b}'.format(dictionary[line]))
    f.close()
    text_out.close()
    return dictionary

def Decode(in_stream, out_stream):
    f = open(in_stream, 'r')        
    dictionary = reset_list()
    text = f.read()    
    text_out = open(out_stream, 'w')
    seq = ""    
    code = ""    
    while True:
        if text == "":
            break
        
        code = text[:16]        
        text = text[16:]        
        index = int(code, 2)

        if len(dictionary) == limit:
            dictionary = reset_list()    
        
        
        if index > len(dictionary):
            raise Exception("Izvan opsega")            
        
        if index == len(dictionary):
            dictionary.append(seq + seq[0])
        elif len(seq) > 0:
             dictionary.append(seq + dictionary[index][0])
        
        text_out.write(dictionary[index])
        seq = dictionary[index]
    
    if len(text) > 0:
        raise Exception("Neispravan fajl")
    f.close()
    text_out.close()
    return dictionary

