#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Elmir Hodzic
"""

import math as m
import cmath as cm
import matplotlib.pyplot as plt;

def fun(t):
    return m.sin(10 * m.pi * t) + 6 * m.sin(20 * m.pi * t) + 2 * m.sin(40 * m.pi * t);


def myDFT(x):
    N = len(x)
    X = []
    for k in range(N):
        sum = complex(0);
        imag = complex(0,1)
        for n in range(N):
            sum += x[n] * cm.exp(- imag * 2 * cm.pi * n * k / N)
        X.append(abs(sum)/100.0)
    return X;


x = [i * 0.01 for i in range(100)]
f = [fun(x[i]) for i in range(100)]

plt.subplot(2, 1, 1)
plt.plot(x, f);
plt.ylabel('y');
plt.xlabel('x');
plt.title('Function');
plt.grid(True);

a = [ i for i in range(100)]
b = myDFT(f)

plt.subplot(2, 1, 2)
plt.stem(a, b, 'b');
plt.ylabel('|F(x)|');
plt.xlabel('');
plt.axis([0, len(a)//2, 0, 5])
plt.title('DFT');
plt.grid(True);
plt.show();
