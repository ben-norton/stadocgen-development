from pathlib import Path
import pandas as pd
import os

# 1.  Create copy of source csv
src = '../../../data/ltc/ltc-source/mapping/ltc_sssom_mapping.csv'
filepath = Path(src)
targetpath = filepath.parents[2] / 'ltc-docs'
sssom_targetpath = filepath.parents[2] / 'ltc-docs'
sssom_df = pd.read_csv(src, encoding='utf8')

# 2. Place copy in new folder with new filename
sssom_csv = os.path.join(targetpath,r'ltc-sssom.csv')
sssom_df.to_csv(sssom_csv, index=False, encoding='utf8')

# Create Term Column with Machine-readable version of the term
sssom_df['term_local_name'] = sssom_df['subject_id']
sssom_df['term_local_name'] = sssom_df['term_local_name'].str.replace('http://rs.tdwg.org/ltc/terms/', '')
sssom_df['term_local_name'] = sssom_df['term_local_name'].str.replace('http://purl.org/dc/terms/', '')
sssom_df['term_local_name'] = sssom_df['term_local_name'].str.replace('http://rs.tdwg.org/dwc/terms/', '')
sssom_df['term_local_name'] = sssom_df['term_local_name'].str.replace('https://schema.org/', '')
sssom_df['term_local_name'] = sssom_df['term_local_name'].str.replace('http://rs.tdwg.org/chrono/terms/', '')

# Create compound name to identify each term within the scope of a class
sssom_df['compound_name'] = sssom_df[["subject_category", "term_local_name"]].apply(".".join, axis=1)
# Create Term URI Column
sssom_df['term_uri'] = sssom_df['subject_id']

sssom_df.to_csv(sssom_csv, index=False, encoding='utf8')