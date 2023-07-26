import csv
import pandas as pd
import numpy as np

df1 = pd.read_csv("../data/ltc-set/ltc-terms-list.csv", encoding="utf8")
df2 = pd.read_csv("../data/ltc-set/ltc-namespaces.csv", encoding="utf8")

df3 = pd.merge(df1, df2[['namespace', 'namespace_uri']], on='namespace', how='inner')
