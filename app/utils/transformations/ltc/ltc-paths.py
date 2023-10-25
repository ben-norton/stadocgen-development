from pathlib import Path
import pandas as pd
import os

# Create copy of source csv
src = '../../../data/ltc/ltc-source/ltc_terms_source.csv'
filepath = Path(src)
targetpath = filepath.parents[1] / 'ltc-docs'
ltc_source_df = pd.read_csv(src, encoding='utf8')
# Place copy in new folder with new filename
ltccsv = os.path.join(targetpath,r'ltc-terms.csv')
ltc_source_df.to_csv(ltccsv, index=False, encoding='utf8')

