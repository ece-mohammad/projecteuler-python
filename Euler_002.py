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
    return not (num & 1)

print(sum(filter(IsEven, GenerateFib(4e6))))

print(time() - ss)
