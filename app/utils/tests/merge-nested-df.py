import pandas as pd
from jinja2 import Template

terms_csv = '../../data/ltc/ltc-docs/ltc-termlist-list.csv'
terms_df = pd.read_csv(terms_csv, encoding='utf8')

skoscsv = '../../data/ltc/ltc-docs/ltc-skos.csv'
skos_df = pd.read_csv(skoscsv, encoding='utf8')

skos_list = []
for index, row in skos_df.iterrows():
    skos_list.append([row.term_uri, row.skos_mappingRelation, row.related_termName])

terms = terms_df.merge(
    skos_df.groupby('term_uri')['term_uri', 'skos_mappingRelation', 'related_termName'].apply(list).reset_index()
)

ltcdf = pd.merge(
    terms_df, skos_df[['term_uri', 'skos_mappingRelation', 'related_termName']], on=['term_uri'], how='left'
)
ltcdf3 = terms_df.merge(
    skos_df[['term_uri', 'skos_mappingRelation', 'related_termName']], on=['term_uri'], how='right'
)
terms.to_csv('termlist.csv',index=False)
ltcdf.to_csv('ltcdf.csv',index=False)
ltcdf3.to_csv('ltcdf3.csv',index=True)
