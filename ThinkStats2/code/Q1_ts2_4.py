import nsfg
import numpy as np


# -- read data into frame --
df = nsfg.ReadFemPreg()

# -- get first and other children data on successful pregnancy --
firsts = df[df.outcome == 1][df.birthord == 1]
others = df[df.outcome == 1][df.birthord != 1]

# -- get weight data --
wgts_first = firsts['totalwgt_lb']
wgts_others = others['totalwgt_lb']


def CohensD(dat1, dat2):
    """ return Cohen's D of two sets of data"""
    mean1 = dat1.mean()
    mean2 = dat2.mean()
    var1 = dat1.var()
    var2 = dat2.var()
    n1 = len(dat1)
    n2 = len(dat2)
    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    return (mean1 - mean2) / np.sqrt(pooled_var)

print "Cohen's D = ", CohensD(wgts_first, wgts_others)
