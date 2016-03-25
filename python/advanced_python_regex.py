import re
import pandas as pd


def cleanDegree(s):
    return re.sub('\s*(\w\w)[\.]?(\w)[\.]?', r' \1.\2.', s)


def cleanTitle(s):
    return re.sub('(.*)Professor.*', r'\1Professor', s)


def emailDomain(s):
    r = re.search('@(.*)', s.strip())
    return r.group(1)


df = pd.read_csv('faculty.csv')
df['degree_cleaned'] = df[' degree'].apply(cleanDegree)
df['title_cleaned'] = df[' title'].apply(cleanTitle)
print df.groupby('degree_cleaned')['name'].count()
print df.groupby('title_cleaned')['name'].count()
print df[' email']

df['email_domain'] = df[' email'].apply(emailDomain)
print df.groupby('email_domain')['name'].count()
