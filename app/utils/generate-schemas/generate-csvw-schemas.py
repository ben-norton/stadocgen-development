from pathlib import Path
from cow_csvw.csvw_tool import COW
import os

# https://github.com/CLARIAH/COW/wiki
#

namespace = 'ltc'
current_dir = Path().absolute()
path = current_dir.parent.parent
csvPath = str(path)+'/data/'+namespace+'/'+namespace+'-source'
outputPath = str(path)+'/data/'+namespace+'/schemas/csvw-schemas'

# giving file extension
ext = ('.csv')

# iterating over all files
for files in os.listdir(csvPath):
    if files.endswith(ext):
        print(files) # printing file name of desired extension
        datasetName = files
        csvw = COW(mode='build', files=[os.path.join(csvPath, files)], dataset=files, delimiter=',', quotechar='\"')

        print(csvw)


    else:
        continue
