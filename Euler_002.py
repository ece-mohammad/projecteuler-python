#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

from time import time

ss = time()

def GenerateFib(limit):
    a, b = 0, 1
    while(b < limit):
        a,b = b, a+b
        yield b

def IsEven(num):
    #& bitwise AND.. All evcen numbers in binary have the LSB (bit 0) = 0
    #so, x AND 1 will equal 0 if the number is even (LSB is 0) or 1 when odd (LSB is 1)
    return not (num & 1)

print(sum(filter(IsEven, GenerateFib(4e6))))

print(time() - ss)
