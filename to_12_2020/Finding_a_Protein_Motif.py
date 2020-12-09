#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 18:06:45 2020

@author: kacper
"""
"""
Problem
To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: 
[XY] means "either X or Y" and {X} means "any amino acid except X." For example,
the N-glycosylation motif is written as N{P}[ST]{P}.

You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt database,
by inserting the ID number into

Given: At most 15 UniProt Protein Database access IDs.

Return: For each protein possessing the N-glycosylation motif,
output its given access ID followed by a list of locations in the protein string where the motif can be found.
"""

import re
import requests
from itertools import groupby



def fasta_parser_seq ( f_name ) :
    """Given : a filename with fasta formatted text
    Return: parsed fasta file, as header + sequence
    """
    
    with open(f_name) as fh:
        fait = (x[1] for x in groupby( fh, lambda line: line[0] == ">"))
        for header in fait:
            headerStr = header.__next__()[1:].strip()
            seq = "".join(s.strip() for s in fait.__next__())
        return  headerStr, seq
            
def n_ac_find ( sequence ):
    """Given : a sequence of prot
    Return  : a list of places where N-glycosylation starts
    """
    macze = re.finditer('(?=([N][^P][TS][^P]))', sequence)
    if macze:
        pcs = [m.start(0)+1 for m in macze]
    else:
        return 0
    return pcs
#+1 as rosalind seems to start counting from 1 on that one...
# a| b  matches either a or b
# [^...] matches any single character not in brackets
# (?=(...))  for overlaping results

def ID_to_url ( ID ):
    """Given: Prot ID
    Return  : an url to open fasta formatted protein info header + seq
    """
    fasta_id = "http://www.uniprot.org/uniprot/%s.fasta"
    return (fasta_id % ID.rstrip())
    #return fasta_id[:31]+ID.rstrip()+fasta_id[31:]

def ofira( filename ) :  
    """ Given  : path to file containing protein ID's
        Return : tab of url adresses to get fasta formats of given protein
    """
    with open (filename) as dane_in:
        ID_tab  = [ line.rstrip() for line in dane_in]
    return ID_tab

def write_fasta_to_temp_file ( fasta_text ) :
    """writes fasta text to a temporary file
    """
    with open ("temp_fasta.txt", 'w') as fasta:
        fasta.write(fasta_text)

def read_file_p ():
    """ reads temp file for check purposes"""
    with open("temp_fasta.txt") as ttt:
        print(ttt.read())

def get_fasta_from_url ( address ):
    """Gets address 
        Returns fasta formatted text
    """
    res = requests.get(address)
    assert res.status_code == 200
    write_fasta_to_temp_file(res.text)

def gffu ( filename ) : 
    ID_tab = ofira(filename)
    """Given  : an arry of ID's and an array of url's
       Return : a dict of { ID : FASTA string }
    """
    dict_fasta = {}
    for  ID in ID_tab:
        #print(ID_to_url(ID))
        #read_file_p()
        get_fasta_from_url(ID_to_url(ID) )
        _, seq = fasta_parser_seq("temp_fasta.txt")
        dict_fasta[ID] = n_ac_find(seq) 
        if dict_fasta[ID] == []:
            del dict_fasta[ID]
    return dict_fasta

def convert_list_to_string(org_list, seperator=' '):
    """ Convert list to string, by joining all item in list with given separator.
        Returns the concatenated string """
    return seperator.join(org_list)
  
def generate_ans( filepath ):
    """Given: filepath to file containing ID of proteins
    Return : a file with prot ID followed by \n followed by places of 
             N-glycosylation motif, in rosalind answer format.
             dip - dict_id_places
    """
    dip = gffu(filepath)
    with open("odp.txt",'w') as out_p:
        for ID in dip:
            out_p.write(ID)
            out_p.write('\n')
            out_p.write(str(dip[ID]).strip('[]').replace(',',''))
            out_p.write('\n')
