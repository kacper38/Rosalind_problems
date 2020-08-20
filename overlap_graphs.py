#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 12:21:31 2020

@author: kacper
"""
"""
Given: A collection of DNA strings in FASTA format having total length at most 10 kbp.

Return: The adjacency list corresponding to O3. You may return edges in any order.
"""

from itertools import groupby, combinations

def fasta_parser ( f_name ) :
    
    with open(f_name) as fh:
        fait = (x[1] for x in groupby( fh, lambda line: line[0] == ">"))

        for header in fait:
            headerStr = header.__next__()[1:].strip()
            seq = "".join(s.strip() for s in fait.__next__())
            yield (headerStr, seq)
        
def fasta_2_dict( tau ):
    fdict = {}
    for ff in fasta_parser(tau):
        headerStr, seq = ff
        fdict[headerStr] = seq
    return fdict

def is_overlap(k1,k2):
    return k1[-3:] == k2[:3]

def adjacency_list_generato ( fd ):
    list1 = []
    for k1, k2 in combinations(fd,2):
        temp1, temp2 = fd.get(k1), fd.get(k2)
        if is_overlap(temp1,temp2):
            list1.append(str(k1) + " " + str(k2))
        if is_overlap(temp2,temp1):
            list1.append(str(k2) + " " + str(k1))
    return(list1)


def main():
    
    with open("/.../odpo3.txt", 'w') as odp:
        for item in adjacency_list_generato(fasta_2_dict("/home/kacper/Dokumenty/rosal/overlap_graphs/rosalind_grph1.txt")):
            odp.write("%s\n" % str(item)  )
            
        
if __name__ == "__main__":
    main()

