

with open("./rosalind_tree.txt", 'rt') as fin:
    n = int(fin.readline().strip('\n').strip())
    cont = [x.strip() for x in fin.readlines()]
    ad = []
    for line in cont:
        s = line.split(' ')
        ad.append([int(s[0]), int(s[1])])

result = n-1-len(ad)
