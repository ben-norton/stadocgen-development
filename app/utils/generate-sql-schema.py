import pandas as pd
import os
from pathlib import Path
import numpy as np

# Create Database Schema from CSV Files that contain database schema information (table name, column name, etc.)

src = '../data/ltc/ltc-docs/ltc-terms-list.csv'
filepath = Path(src)
targetpath = filepath.parents[1] / 'ltc-docs'
ltc_source_df = pd.read_csv(src, encoding='utf8')
# 2. Place copy in new folder with new filename
ltccsv = os.path.join(targetpath,r'ltc-terms-sql.csv')
ltc_source_df.to_csv(ltccsv, index=False, encoding='utf8')

newsrc = '../../data/ltc/ltc-docs/ltc-terms-sql.csv'
df = pd.read_csv(newsrc, encoding="utf8")
df.rename(columns={'term_local_name':'COLUMN', 'class_name':'TABLE', 'datatype':'TYPE'}, inplace=True)
df2 = df[['TABLE','COLUMN','TYPE']].dropna()
df2['TYPE'] = df2['TYPE'].replace(to_replace ='array<ltc:[A-z]+>', value = 'integer', regex = True)
df2.set_index('TABLE')
#print(df2)



df3 = df2[df2["COLUMN"].str.contains("has")][['TABLE','COLUMN']]
df3['COLUMN'] = df3['COLUMN'].str.replace(r'has', ' ||--o{ ', regex=False)
df3['COLUMN'] = df3['COLUMN'].astype(str) + ' : "Has"'
df3['TABLE_ASSOCIATIONS'] = df3['TABLE'].astype(str) + df3["COLUMN"]
print(df3['TABLE_ASSOCIATIONS'].tolist())

#np.savetxt("GFG.csv",lst,delimiter =", ",fmt ='% s')
