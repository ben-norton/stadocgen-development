import pandas as pd

csvfile = '../../data/ltc/ltc-docs/ltc-sssom.csv'
df = pd.read_csv(csvfile)
df1 = df.groupby(['subject_id','subject_label']).size().reset_index(name='count')
df2 = df.groupby(['subject_id','subject_label']).filter(lambda x: len(x) > 1)
print(df2)
