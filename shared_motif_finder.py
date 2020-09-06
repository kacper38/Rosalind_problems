#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 13:48:08 2020

@author: kacper
"""
from itertools import groupby

def fasta_parser ( f_name ) :
    
    with open(f_name) as fh:
        fait = (x[1] for x in groupby( fh, lambda line: line[0] == ">"))

        for header in fait:
            #no need for header / optional
            #headerStr = header.__next__()[1:].strip()
            seq = "".join(s.strip() for s in fait.__next__())
            yield (seq) # if with header, go (headerStr, seq)

list_sq = [x for x in fasta_parser("rosalind_lcsm.txt")]


is_common_substr = lambda s, strings: all(s in x for x in strings)
#wpa = ['aaaaaaaaaaa','bbbbb','cc','ccc']


def long_substr(data):
    sub = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(sub) and is_common_substr(data[0][i:i+j],data):
                    sub = data[0][i:i+j]
    return sub




def longestCommon(seqs):
  shortest = min(seqs, key=len)
  for length in range(len(shortest), 0, -1):
    for start in range(len(shortest) - length + 1):
      sub = shortest[start:start+length]
      if all(seq.find(sub) >= 0 for seq in seqs):
        return sub
  return ""


#answer ->
print(long_substr(list_sq),'\n')
#or
print(longestCommon(list_sq))
