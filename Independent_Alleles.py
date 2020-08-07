from itertools import product
from scipy.special import binom
from scipy.stats import binom

""" 
probability of a specimen with genotype AaBb
is always the same given the AaBb mates
checked it, by doing 9 punnet squares on paper..
"""


def probability(k, N):
    P = 2**k
    p = 0
    for i in range(N, P + 1):
        pr = binom(P, i) * (0.25**i) * (0.75**(P-i))
        p += pr
    return float("{:.3f}".format(p))
    
    
    def prob_cdf(k, N, p):
    return float("{:.3f}".format(  binom.cdf(k, N, p)))

""" as cdf is somewhat not accurate, by 0,02 (a lot!)
scipy.stats.binom suggest using survival function
described as 1 - cdf,  so i use that and got the same results
as applying the formula by hand in [probability]
"""   
n = 34
k = 7
def p2(k,N):
    return(float("{:.3f}".format(binom.sf(N - 1, 2**k, 0.25))))
