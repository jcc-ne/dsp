import re
import pandas as pd
from collections import OrderedDict
from operator import itemgetter


def cleanDegree(s):
    return re.sub('\s*(\w\w)[\.]?(\w)[\.]?', r' \1\2', s)


def cleanTitle(s):
    return re.sub('(.*)Professor.*', r'\1Professor', s)


df = pd.read_csv('faculty.csv')
df['degree_cleaned'] = df[' degree'].apply(cleanDegree)
df['title_cleaned'] = df[' title'].apply(cleanTitle)
df['lastname'] = df['name'].apply(lambda x: x.split()[-1])
df['firstname'] = df['name'].apply(lambda x: x.split()[0])

# groupby lastname
dic = OrderedDict()
for g in df.groupby('lastname'):
    dic[g[0]] = g[1][['degree_cleaned', 'title_cleaned', ' email']].values
for k, v in dic.iteritems():
    print k, v

# groupby both first and lastname
dic2 = OrderedDict()
for g in df.groupby(['firstname', 'lastname']):
    dic2[g[0]] = g[1][['degree_cleaned', 'title_cleaned', ' email']].values

for k, v in dic2.iteritems():
    print k, v

# sort by lastname
for k in sorted(dic2, key=itemgetter(1)):
    print dic2[k]
