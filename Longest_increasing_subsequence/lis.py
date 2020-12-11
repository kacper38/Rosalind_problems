import os

ppath = os.getcwd()

#%%

with open('/home/kacper/PycharmProjects/Rosalind_problems/enumerating_kmers_lexicographically/rosalind_lgiss.txt','r') as din:
    lines = [line.rstrip() for line in din]

nums = [int(x.strip()) for x in lines[1].split()]
length = int(lines[0])

def subsequence(seq, increasing = True):
    if not seq:
        return seq

    M = [None] * len(seq)
    P = [None] * len(seq)

    L = 1
    M[0] = 0


    for i in range(1, len(seq)):

        lower = 0
        upper = L

        if increasing == True and seq[M[upper-1]] < seq[i]:
            j = upper
        elif increasing == False and seq[M[upper-1]] > seq[i]:
            j = upper
        else:
            while upper - lower > 1:
                mid = (upper + lower) // 2
                if increasing == True and seq[M[mid-1]] < seq[i]:
                    lower = mid
                elif increasing == False and seq[M[mid-1]] > seq[i]:
                    lower = mid
                else:
                    upper = mid

            j = lower

        P[i] = M[j-1]

        if increasing == True and (j == L or seq[i] < seq[M[j]]):
            M[j] = i
            L = max(L, j+1)
        elif increasing == False and (j == L or seq[i] > seq[M[j]]):
            M[j] = i
            L = max(L, j+1)

    result = []
    pos = M[L-1]
    for _ in range(L):
        result.append(seq[pos])
        pos = P[pos]

    return result[::-1]

inc = subsequence(nums,increasing=True)
dec = subsequence(nums,increasing=False)

incs = ""
for el in inc:
    incs += str(el)+' '
decs = ""
for el in dec:
    decs += str(el)+' '

with open('fout.txt', 'w') as fout:
    fout.write(incs+"\n")
    fout.write(decs)

print(*inc, sep=' ')
print(*dec, sep=' ')
