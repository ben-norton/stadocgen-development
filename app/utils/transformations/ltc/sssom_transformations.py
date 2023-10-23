from pathlib import Path
import pandas as pd
import os

# 1.  Create copy of source csv
src = '../../../data/ltc/ltc_source/mapping/ltc_sssom_mapping.csv'
filepath = Path(src)
targetpath = filepath.parents[2] / 'ltc_docs'
sssom_source_df = pd.read_csv(src, encoding='utf8')

# 2. Place copy in new folder with new filename
sssomcsv = os.path.join(targetpath,r'ltc_sssom.csv')
sssom_source_df.to_csv(sssomcsv, index=False, encoding='utf8')

newsrc = '../../../data/ltc/ltc_docs/ltc_sssom.csv'
sssom_df = pd.read_csv(newsrc, encoding="utf8")
sssom_df = sssom_df.drop_duplicates(keep='first')
sssom_df.to_csv(newsrc, index=False, encoding='utf8')

# Add Term URI Column for Relationship
sssom_df['term_uri'] = sssom_df['subject_id']
# Write Result to File
sssom_df.to_csv(newsrc, index=False, encoding='utf8')

