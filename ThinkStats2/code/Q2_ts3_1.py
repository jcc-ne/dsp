import thinkstats2
import thinkplot


def BiasedPmf(pmf0):
    """ return renormalized biased pmf toward the sample values """
    pmf = pmf0.Copy()
    for x, p in pmf.Items():
        pmf.Mult(x, x)
    pmf.Normalize()
    return pmf


def readNplotNUMKDHH(dctfile='2002FemResp.dct',
                     datfile='2002FemResp.dat.gz',
                     compression='gzip'):
    """ read data to fram and plot NUMKDHH PMF"""
    dct = thinkstats2.ReadStataDct(dctfile)
    df = dct.ReadFixedWidth(datfile, compression=compression)

    pmf = thinkstats2.Pmf(df.numkdhh)
    thinkplot.Pmf(pmf, label='numkdhh')

    pmf2 = BiasedPmf(pmf)
    thinkplot.Pmf(pmf2, label='biased')
    thinkplot.show()


readNplotNUMKDHH()
