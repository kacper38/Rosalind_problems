import os

def union(a,b):
    c = a.copy()
    c |= b
    return c

def intersection(a,b):
    return set([x for x in a if x in b])

def a_minus_b(a,b):
    return set([x for x in a if x not in b])

def b_minus_a(a,b):
    return set([x for x in b if x not in a])

def a_superscript_C(a,n):
    return set([x for x in range(1,n+1) if x not in a])

#%%

with open("subsets_tasks/rosalind_seto.txt", 'rt') as din:
    for i, line in enumerate(din.readlines()):
        if i == 0:
            n = int(line.strip('\n'))
        elif i == 1:
            q = set([int(x.strip(',').strip('{').strip('}')) for x in line.split()])
        elif i == 2:
            w = set([int(x.strip(',').strip('{').strip('}')) for x in line.split()])

#n = int(xg[0].strip('\n'))
#q = set([ int(ent) for ent in xg[1].strip('\n') if ent.isdigit()])
#w = set([int(ent) for ent in xg[2].strip('\n') if ent.isnumeric()])
with open("subsets_tasks/odp.txt", 'wt') as dout:
    dout.write(str(union(q,w))+'\n')
    dout.write(str(intersection(q,w))+'\n')
    dout.write(str(a_minus_b(q,w))+'\n')
    dout.write(str(b_minus_a(q,w))+'\n')
    dout.write(str(a_superscript_C(q,n))+'\n')
    dout.write(str(a_superscript_C(w,n))+'\n')

'''    
print(union(q,w))
print(intersection(q,w))
print(a_minus_b(q,w))
print(b_minus_a(q,w))
print(a_superscript_C(q,n))
print(a_superscript_C(w,n))
'''