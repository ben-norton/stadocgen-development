import pandas as pd

src = '../../../data/ltc/ltc-docs/ltc-terms-list.csv'

ltf_df = pd.read_csv(src, encoding="utf8")
ltf_df.rename(columns={'tdwgutility_organizedInClass':'class_name','tdwgutility_required':'is_required','tdwgutility_repeatable':'is_repeatable'}, inplace=True)

ltf_df['is_required'] = ltf_df['is_required'].replace({'Yes': 'True'})
ltf_df['is_required'] = ltf_df['is_required'].replace({'No': 'False'})
ltf_df['is_repeatable'] = ltf_df['is_repeatable'].replace({'Yes': 'True'})
ltf_df['is_repeatable'] = ltf_df['is_repeatable'].replace({'No': 'False'})
ltf_df.to_csv(src, index=False)