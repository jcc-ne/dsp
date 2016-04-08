# blue men question
import scipy.stats as st

def convertToCm(ft=0.0, inch=0.0):
    return ft * 12 * 2.54 + inch * 2.54

mu = 178.
sigma = 7.7

norm = st.norm(loc=mu, scale=sigma)

# converting units
ht_low = convertToCm(5, 10)
ht_high = convertToCm(6, 1)

low = norm.cdf(ht_low)
high = norm.cdf(ht_high)

print "{:.2%} of male population are in the range of Blue Men height".\
    format(high - low)
