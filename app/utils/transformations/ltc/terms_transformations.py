from pathlib import Path
import pandas as pd
import os

# 1.  Create copy of source csv
src = '../../../data/ltc/ltc-source/ltc_terms_source.csv'
filepath = Path(src)
targetpath = filepath.parents[1] / 'ltc-docs'
ltc_source_df = pd.read_csv(src, encoding='utf8')
# 2. Place copy in new folder with new filename
ltccsv = os.path.join(targetpath,r'ltc-terms-list.csv')
ltc_source_df.to_csv(ltccsv, index=False, encoding='utf8')

ns_csv = '../../../data/ltc/ltc-docs/ltc-namespaces.csv'
newsrc = '../../../data/ltc/ltc-docs/ltc-terms-list.csv'

ltc_df = pd.read_csv(newsrc, encoding="utf8")
# Rename Columns
ltc_df.rename(columns={'term_localName':'term_local_name','tdwgutility_organizedInClass':'class_name','tdwgutility_required':'is_required','tdwgutility_repeatable':'is_repeatable'}, inplace=True)
# Update to boolean value standard
ltc_df['is_required'] = ltc_df['is_required'].replace({'Yes': 'True'})
ltc_df['is_required'] = ltc_df['is_required'].replace({'No': 'False'})
ltc_df['is_repeatable'] = ltc_df['is_repeatable'].replace({'Yes': 'True'})
ltc_df['is_repeatable'] = ltc_df['is_repeatable'].replace({'No': 'False'})
# Create compound name column to uniquely identify each record
ltc_df['compound_name'] = ltc_df[["class_name", "term_local_name"]].apply(".".join, axis=1)
# Add namespaces URIs
ns_df = pd.read_csv(ns_csv, encoding="utf8")
ltc_df = pd.merge(ltc_df, ns_df[['namespace', 'namespace_uri']], on='namespace', how='inner')

# Create Term URI
ltc_df['term_uri'] = ltc_df['namespace_uri'].astype(str) + ltc_df['term_local_name']

# Create Term with Namespace Prefix
ltc_df['term_ns_name'] = ltc_df['namespace'].astype(str) + ltc_df['term_local_name']

# Write transformations to file
ltc_df.to_csv(newsrc, index=False, encoding='utf8')





ltc_df = pd.read_csv(newsrc, encoding="utf8")
# Datatypes
dt_src = '../../../data/ltc/ltc-source/ltc_datatypes.csv'
dt_filepath = Path(dt_src)
dt_targetpath = dt_filepath.parents[1] / 'ltc-docs'
dt_ltc_source_df = pd.read_csv(dt_src, encoding='utf8')
# 2. Place copy in new folder with new filename
dt_ltccsv = os.path.join(dt_targetpath,r'ltc-datatypes.csv')
dt_ltc_source_df.to_csv(dt_ltccsv, index=False, encoding='utf8')

# New Datatypes file
dt_newsrc = '../../../data/ltc/ltc-docs/ltc-datatypes.csv'
dt_ltc_df = pd.read_csv(dt_newsrc, encoding="utf8")
# Rename Column
dt_ltc_df.rename(columns={'term_localName':'term_local_name','tdwgutility_organizedInClass':'class_name'}, inplace=True)
dt_ltc_df['compound_name'] = dt_ltc_df[["class_name", "term_local_name"]].apply(".".join, axis=1)
# Write changes to file
dt_ltc_df.to_csv(dt_newsrc, index=False, encoding='utf8')

ltc_df = pd.merge(ltc_df, dt_ltc_df[['compound_name', 'datatype']], on='compound_name', how='left')
# Write CSV to File
ltc_df.to_csv(newsrc, index=False, encoding='utf8')
