import pandas as pd
import os
from pathlib import Path
import numpy as np

# Create Database Schema from CSV Files that contain database schema information (table name, column name, etc.)
current_dir = Path().absolute()
path = current_dir.parent
src = str(path)+'/data/ltc/ltc-docs/ltc-termlist-list.csv'
target = str(path)+'/data/ltc/schemas/sql-schemas'
targetPath = Path(target)
ltc_source_df = pd.read_csv(src, encoding='utf8')
# 2. Place copy in new folder with new filename
ltccsv = os.path.join(targetPath,r'ltc-termlist-sql.csv')
sqlcsv = os.path.join(targetPath,r'ltc-sql.csv')

ltc_source_df.to_csv(ltccsv, index=False, encoding='utf8')

df = pd.read_csv(ltccsv, encoding="utf8")
df.rename(columns={'term_local_name':'COLUMN', 'class_name':'TABLE', 'datatype':'TYPE'}, inplace=True)
df2 = df[['TABLE','COLUMN','TYPE']].dropna()
df2['TYPE'] = df2['TYPE'].replace(to_replace ='array<ltc:[A-z]+>', value = 'integer', regex = True)
df2.set_index('TABLE')
#df2.to_csv(df2csv, index=False, encoding='utf8')

df3 = df2[df2["COLUMN"].str.contains("has")][['TABLE','COLUMN']]
df3['COLUMN'] = df3['COLUMN'].str.replace(r'has', ' ||--o{ ', regex=False)
df3['COLUMN'] = df3['COLUMN'].astype(str) + ' : "Has"'
df3['TABLE_ASSOCIATIONS'] = df3['TABLE'].astype(str) + df3["COLUMN"]
#print(df3['TABLE_ASSOCIATIONS'].tolist())
df3.to_csv(sqlcsv, index=False, encoding='utf8')

#np.savetxt("GFG.csv",lst,delimiter =", ",fmt ='% s')
