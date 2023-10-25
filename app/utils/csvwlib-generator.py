from cow_csvw.csvw_tool import COW
import os
from pathlib import Path

file = '../data/ltc/ltc-docs/ltc-terms-list.csv'
csvm = COW(mode='build', files=[os.path.join(file)], dataset='LTC Terms', delimiter=',', quotechar='\"', base='https://github.com/tdwg/ltc/source/schemas')
