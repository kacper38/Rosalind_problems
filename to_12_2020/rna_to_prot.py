#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 09:29:40 2020

@author: kacper
"""

def rprotein_string(RNA_string):
    
    rna_codons = {"UUU":"F","UUC":"F","UUA":"L","UUG":"L",
                  "UCU":"S","UCC":"S","UCA":"S","UCG":"S",
                  "UAU":"Y","UAC":"Y","UAA":"","UAG":"",
                  "UGU":"C","UGC":"C","UGA":"","UGG":"W",
                  "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
                  "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
                  "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
                  "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
                  "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
                  "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
                  "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
                  "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
                  "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
                  "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
                  "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
                  "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G"}
    
    protein_strings = []
    
    for mer in range (0, len(RNA_string), 3):
        protein_strings.append(RNA_string[mer:mer + 3])
        
    protein_string = ''.join([rna_codons[codon] for codon in protein_strings ] )
    
    return protein_string

def main():
    with open(".../rosalind_prot.txt") as data_in:
        rna_string = data_in.read().rstrip()
        
     #   print(f'{rprotein_string(rna_string)}')
        
    with open(".../odp.txt",'w') as dane_out:
        dane_out.write(rprotein_string(rna_string))
    print(rprotein_string('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA'))
    assert rprotein_string('AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA') == 'MAMAPRTEINSTRING'


if __name__ == '__main__':
    main()
