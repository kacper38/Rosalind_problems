#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 12:20:49 2020

@author: kacper
"""
import math


AT = 0
GC = 0

with open("./rosalind_prob.txt", 'rt') as fin:
    for line in fin:
        for h in line:
            if h =='T' or h =='A':
                AT +=1
            elif h =='C' or h=='G':
                GC +=1
                
        if line[0] != 'A' and line[0] != 'C'\
            and line[0] != 'G' and line[0] != 'T':
            numbers = line.split()
            GC_content = [float(x) for x in numbers]

def probability(AT, GC, number):
    return math.log10( (((1 - number) / 2 )**AT) * ((number/2)**GC))

probs = [ round(probability(AT, GC, x),3) for x in GC_content ]

print(*probs, sep=' ')

