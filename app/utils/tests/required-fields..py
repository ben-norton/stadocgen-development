import pandas as pd
import os
from pathlib import Path


init_csv = '../../data/ltc/ltc-docs/ltc-termlist.csv'
df = pd.read_csv(init_csv, encoding='utf8')

terms_df = df[['namespace', 'term_local_name', 'label', 'class_name',
               'is_required', 'rdf_type', 'compound_name']].sort_values(by=['class_name'])
required_df = terms_df.loc[(terms_df['is_required'] == True) &
                           (terms_df['rdf_type'] == 'http://www.w3.org/1999/02/22-rdf-syntax-ns#Property')]
print(required_df)


