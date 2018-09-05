#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Elmir Hodzic
"""

import math
import matplotlib.pyplot as plt;

def fun(t):
    return math.sin(10 * math.pi * t) + 6 * math.sin(20 * math.pi * t) + 2 * math.sin(40 * math.pi * t);



def filter(data, fc):
    M = len(data);
    filter_output = [];
    
    for m in range(len(data)):
        ym = 0;
        
        for k in range(M):
            hk = math.sin(2*math.pi*fc*(data[m] - M / 2))/(math.pi*(data[m] - M / 2))
            if m >= k:
                ym = ym + hk * data[m - k] 
        
        filter_output.append(ym);

    return filter_output;

x = [i * 0.01 for i in range(100)]
f = [fun(x[i]) for i in range(100)]

plt.subplot(2, 1, 1)
plt.plot(x, f);
plt.ylabel('y');
plt.xlabel('x');
plt.title('Function');
plt.grid(True);

a = [ i for i in range(100)]
b = filter(f, 50)

plt.subplot(2, 1, 2)
plt.plot(a, b, 'r');
plt.ylabel('Filtered signal');
plt.xlabel('x');

plt.title('FIR');
plt.grid(True);
plt.show();