import numpy as np

# -- generate random number
rand = np.random.random(1000)

# --  check its PMF if the results are uniformly distributed
pmf = thinkstats2.Pmf(rand)
thinkplot.Pmf(pmf)
thinkplot.show()

# --  check its CDF if the results are uniformly distributed
cdf = thinkstats2.Cdf(rand)
thinkplot.Cdf(cdf)
thinkplot.show()
