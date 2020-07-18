#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 10:08:43 2020

@author: kacper
"""


def motif_find(data_in):

    plcs = []
    
    for x in range(0,len(data_in[0])):
        #print(data_in[0][x:x+l_sub])
        if data_in[0][x:x+len(data_in[1])] == data_in[1]:
            plcs.append(x+1)
    return (plcs)


def main():
    
    with open("/home/kacper/Dokumenty/rosal/finding_motif/rosalind_subs.txt") as dane_in:
        x = dane_in.read().rstrip().split('\n')
    
    with open("/home/kacper/Dokumenty/rosal/finding_motif/odp.txt", "w") as dane_out:

        for item in motif_find(x):
            dane_out.write(str(item)+' ')

if __name__ == '__main__':
    main()
















