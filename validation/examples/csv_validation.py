# coding: utf-8

import pandas as pd
import numpy as np
import yaml

# Example of CSV Validation using YAML Field Definitions
# https://gist.github.com/vehrka/97649f71238b490ebbdf34de5a738584


# ## Input data file

venues_filename = 'venues.csv'

# ### CSV definition

yaml_csv_setup = """
venues:
    id: int
    longitude: float
    latitude: float
    address: string
    name: string
    capacity: int
    sqrm: int
"""

# ### Data Mapping with numpy types

dict_dtypes = {
    'int': np.dtype('int64'),
    'string': np.dtype('O'),
    'float': np.dtype('float64'),
    'date': np.dtype('O')
}

# ## Data loading in the dataframe

dfs = [pd.read_csv(venues_filaname)]

# ## File validation acording to the definition

csv_setup_dict = yaml.load(yaml_csv_setup)

checks = list(csv_setup_dict.keys())

for i, check in enumerate(checks):
    check_dict = csv_setup_dict[check]
    check_fields = list(check_dict.keys())
    df_check = dfs[i]

    try:
        assert len(df_check.columns) == len(check_fields)
    except AssertionError:
        print('Incorrect number of columns in {}'.format(checks[i]))

    try:
        assert pd.Series(check_fields).isin(df_check.columns).all()
    except AssertionError:
        dfwc = pd.Series(check_fields).isin(df_check.columns)
        dfwcf = dfwc[dfwc == False]
        lmfieldname = [check_fields[i] for i in list(dfwcf.index)]
        print('In the file {} the following columns are missing: {}'.format(checks[i], ", ".join(lmfieldname)))

    try:
        t_defi = [dict_dtypes[check_dict[field]] for field in check_fields]
        t_file = df_check.dtypes.tolist()
        assert t_defi == t_file
    except AssertionError:
        error_file = [(i,x) for i, x in enumerate(t_file) if x not in t_defi]
        if len(error_file) > 0:
            for i, x in error_file:
                print('The field {} type is {} in the file, but it should be {} according to the definiton'.format(check_fields[i], x, check_dict[check_fields[i]] ))
