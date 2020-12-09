#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 18:19:33 2020

@author: kacper
"""
"""
Given: A collection of at most 10 DNA strings of equal length (at most 1 kbp) in FASTA format.

Return: A consensus string and profile matrix for the collection. (If several possible consensus strings exist, then you may return any one of them.)
"""

from itertools import groupby
from numpy import array as arr

def fasta_parser ( f_name ) :
    with open(f_name) as fh:
        fait = (x[1] for x in groupby( fh, lambda line: line[0] == ">"))
        for header in fait:
            seq = "".join(s.strip() for s in fait.__next__())
            yield  seq

path1 = "rosalind_cons.txt"

def pkr(path):
    list_seq = list(fasta_parser(path))
    
    seq_len = len(list_seq[0])
    my_dict = {'A': [0] * seq_len, 'C':[0] * seq_len
               , 'G':[0] * seq_len, 'T':[0] * seq_len}        
    for seq in list_seq:
        for i in range(seq_len):
            if   seq[i] == 'A':
                my_dict['A'][i] += 1
            elif seq[i] == 'C':
                my_dict['C'][i] += 1
            elif seq[i] == 'G':
                my_dict['G'][i] += 1
            else:
                my_dict['T'][i] += 1
    sequa1 = ''
    for i in range(seq_len):
        if my_dict['A'][i] > my_dict['C'][i] and my_dict['A'][i] > my_dict['G'][i] and \
        my_dict['A'][i] > my_dict['T'][i] :
            sequa1 += 'A'
        elif my_dict['C'][i] > my_dict['G'][i] and my_dict['C'][i] > my_dict['T'][i] :
            sequa1 += 'C'
        elif my_dict['G'][i] > my_dict['T'][i] :
            sequa1 += 'G'
        else :
            sequa1 += 'T'
        
    print(sequa1)
    for k,v in my_dict.items():
        print(f"{k}: {str(v).replace(',','')[1:-1]}")
    
#quick numpy version


def rkp(path):
    matrix = arr([arr(list(line.strip())) for line in fasta_parser(path)])
    
    bases = arr(list('ACGT'))
    
    P = arr([(matrix == g).sum(axis=0) for g in bases])
    #P = profile matrix
    consensus = bases[P.argmax(axis=0)]
    consensus = ''.join(consensus)
    
    print (consensus)
    for i, g in enumerate(bases):
        print ('%s:' % g, ' '.join(map(str, P[i])))
    
print(rkp(path1))

"""
seems that naive approach is only 3 quarters of a second slower,
%timeit rkp(path1)
1.98 ms ± 131 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%timeit pkr(path1)
2.77 ms ± 167 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
"""
