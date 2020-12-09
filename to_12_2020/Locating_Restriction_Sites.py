"""
Problem

Figure 2. Palindromic recognition site
A DNA string is a reverse palindrome if it is equal to its reverse complement. For instance, GCATGC is a reverse palindrome because its reverse complement is GCATGC. See Figure 2.

Given: A DNA string of length at most 1 kbp in FASTA format.

Return: The position and length of every reverse palindrome in the string having length between 4 and 12. You may return these pairs in any order.

Sample Dataset
>Rosalind_24
TCAATGCATGCGGGTCTATATGCAT
Sample Output
4 6
5 4
6 6
7 4
17 4
18 4
20 6
21 4
"""
"""
Created on Sun Sep  6 14:13:28 2020

@author: kacper
"""

from itertools import groupby
def fasta_parser ( f_name ) :
    with open(f_name) as fh:
        fait = (x[1] for x in groupby( fh, lambda line: line[0] == ">"))
        for header in fait:
            seq = "".join(s.strip() for s in fait.__next__())
            return(  seq)
            
def reverse(seq):
    tab = str.maketrans("ACTG","TGAC")
    return (seq.translate(tab)[::-1])

def irp(seq):
    #is_reverse_palindrome
    return (seq == reverse(seq) )

def return_pos_len(seq):
    N= len(seq)
    flag = lambda x,y,seqw : irp(seqw[x:x+y]) == True
    return([[j+1,i] for i in range(4,13) for j in range(0, N-i+1) if flag(j,i,seq)])

def pos_and_length(f_name):
    answ = return_pos_len(fasta_parser(f_name))
    with open("odp_lrs.txt", 'w') as ans:
        for item in answ:
            print(' '.join(map(str,item)))
            ans.write(' '.join(map(str, item)))
            ans.write("\n")
                
