from pathlib import Path
import pandas as pd
import os

# 1.  Create copy of source csv
src = '../../../data/ltc/ltc_source/mapping/ltc_skos_mapping.csv'
filepath = Path(src)
targetpath = filepath.parents[2] / 'ltc_docs'
skos_source_df = pd.read_csv(src, encoding='utf8')

# 2. Place copy in new folder with new filename
skoscsv = os.path.join(targetpath,r'ltc_skos.csv')
skos_source_df.to_csv(skoscsv, index=False, encoding='utf8')

newsrc = '../../../data/ltc/ltc_docs/ltc_skos.csv'
skos_df = pd.read_csv(newsrc, encoding="utf8")
skos_df = skos_df.drop_duplicates(keep='first')
skos_df.rename(columns={'term_localName':'term_uri'}, inplace=True)
skos_df.to_csv(newsrc, index=False, encoding='utf8')

# Add Term Name and Term with Namespace Prefix Columns
skos_df['term_local_name'] = skos_df['term_uri']
skos_df['term_local_name'] = skos_df['term_local_name'].str.replace('http://rs.tdwg.org/ltc/terms/', '')
skos_df['term_ns_name'] = 'ltc:' + skos_df['term_local_name']
# Write Result to File
skos_df.to_csv(newsrc, index=False, encoding='utf8')

