from pathlib import Path
import pandas as pd
import os
import shutil

namespace = 'ltc'
current_dir = Path().absolute()
path = current_dir.parent.parent.parent


# 1.  Create copy of source csv
skos_src = str(path)+'/data/ltc/ltc-source/mapping/ltc_skos_mapping.csv'
skos_csv = str(path)+'/data/ltc/ltc-docs/ltc-skos.csv'
shutil.copy(skos_src, skos_csv)

skos_df = pd.read_csv(skos_csv, encoding='utf8')
skos_df = skos_df.drop_duplicates(keep='first')
skos_df.rename(columns={'term_localName': 'term_iri'}, inplace=True)

#skos_df.to_csv(skos_csv, index=False, encoding='utf8')

# Add Term Name and Term with Namespace Prefix Columns
skos_df['term_local_name'] = skos_df['term_iri']
skos_df['term_local_name'] = skos_df['term_local_name'].str.replace('http://rs.tdwg.org/ltc/terms/', '')
skos_df['term_ns_name'] = 'ltc:' + skos_df['term_local_name']
# Write Result to File

skos_df.to_csv(skos_csv, index=False, encoding='utf8')
