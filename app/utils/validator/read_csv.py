import csv
import pandas as pd

# open the file in read mode
csvfile = '../../data/ltc/ltc_docs/ltc_terms_list.csv'

data = pd.read_csv(csvfile)
df = pd.DataFrame(data)
uniques = df['datatype'].unique()
print(uniques)

# creating dictreader object
file = open(csvfile, 'r')
csv_reader = csv.DictReader(file)
dict_from_csv = dict(list(csv_reader)[0])
col_names = list(dict_from_csv.keys())
print(col_names)