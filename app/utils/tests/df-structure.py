import pandas as pd

csvfile = '../data/ltc/ltc-docs/ltc-termlist-list.csv'
df = pd.read_csv(csvfile, encoding='utf8')
pd.options.display.max_colwidth = 1200
df.term_local_name = df.term_local_name.apply(lambda row: row.lstrip(' '))
df['term_datatype'] = df['term_local_name'] + ' : ' + df['datatype']
df2 = df.groupby('class_name')['term_datatype'].apply(list)
with open("file.txt", 'w') as output:
    output.write(str(df2))
