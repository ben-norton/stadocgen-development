from cow_csvw.csvw_tool import COW
import os
from pathlib import Path

file = '../../archive/csv/ltc/20231207/ltc-docs/ltc-terms-list.csv'
csvm = COW(mode='build', files=[os.path.join(file)], dataset='LTC Terms', delimiter=',', quotechar='\"', base='https://github.com/tdwg/ltc/source/schemas')
