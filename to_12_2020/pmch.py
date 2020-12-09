#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Problem
A perfect matching on the basepair edges is highlighted in red and represents a candidate secondary structure for the RNA strand.
A matching in a graph G is a collection of edges of G for which no node belongs to more than one edge in the collection. See Figure 2 for examples of matchings. If G contains an even number of nodes (say 2n), then a matching on G is perfect if it contains n edges, which is clearly the maximum possible. An example of a graph containing a perfect matching is shown in Figure 3.

First, let Kn denote the complete graph on 2n labeled nodes, in which every node is connected to every other node with an edge, and let pn denote the total number of perfect matchings in Kn. For a given node x, there are 2n−1 ways to join x to the other nodes in the graph, after which point we must form a perfect matching on the remaining 2n−2 nodes. This reasoning provides us with the recurrence relation pn=(2n−1)⋅pn−1; using the fact that p1 is 1, this recurrence relation implies the closed equation pn=(2n−1)(2n−3)(2n−5)⋯(3)(1).

Given an RNA string s=s1…sn, a bonding graph for s is formed as follows. First, assign each symbol of s to a node, and arrange these nodes in order around a circle, connecting them with edges called adjacency edges. Second, form all possible edges {A, U} and {C, G}, called basepair edges; we will represent basepair edges with dashed edges, as illustrated by the bonding graph in Figure 4.

Note that a matching contained in the basepair edges will represent one possibility for base pairing interactions in s, as shown in Figure 5. For such a matching to exist, s must have the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

Given: An RNA string s of length at most 80 bp having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'.

Return: The total possible number of perfect matchings of basepair edges in the bonding graph of s.

Sample Dataset
>Rosalind_23
AGCUAGUCAU
Sample Output
12
"""
"""
Created on Tue Sep  8 15:45:41 2020

@author: kacper
"""
from math import factorial
from itertools import groupby


def fasta_parser ( f_name ) :
    with open(f_name) as fh:
        fait = (x[1] for x in groupby( fh, lambda line: line[0] == ">"))
        for header in fait:
            seq = "".join(s.strip() for s in fait.__next__())
            return(  seq)


def nobo(seq, base):
    """no_of_base_occurences"""
    #return sum([1 for x in seq if x == base])
    return seq.count(base)


def tpn(f_name):
    seq = fasta_parser (f_name)
    #no_A, no_C = nobo(seq,'A') , nobo(seq, 'C')
    #return factorial(no_A) * factorial(no_C)
    return factorial(seq.count('A')) * factorial(seq.count('G'))
