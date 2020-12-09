#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:49:47 2020

@author: kacper
"""


def mass_of_P(P):
    '''
    Given: A protein string P of length at most 1000 aa.
    Return: The total weight of P.
    '''
    
    mass_dict = {'A':71.03711,  'C':103.00919, 'D':115.02694, 'E':129.04259, 
             'F':147.06841, 'G':57.02146,  'H':137.05891, 'I':113.08406,
             'K':128.09496, 'L':113.08406, 'M':131.04049, 'N':114.04293,
             'P':97.05276,  'Q':128.05858, 'R':156.10111, 'S':87.03203,
             'T':101.04768, 'V':99.06841,  'W':186.07931, 'Y':163.06333 }
    
    total_weight = sum( mass_dict[letter] for letter in P)
    
    return round(total_weight,3)
    
    
def main():
    
    with open("/.../rosalind_prtm.txt") \
    as protein_string:       
        total_weight_of_P = mass_of_P( protein_string.read().rstrip())
    with open("/.../odp_mass.txt",'w') as dane_out:
        dane_out.write(str(total_weight_of_P))
        
if __name__ == "__main__" :
    main()
