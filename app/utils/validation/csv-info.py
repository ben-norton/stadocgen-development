import os
from pathlib import Path
from cow_csvw.csvw_tool import COW
import csv


namespace = 'ltc'
current_dir = Path().absolute()
path = current_dir.parent.parent
basePath = str(path)+'/data/'+namespace+'/'+namespace+'-source/'
outputPath = str(path)+'/data/'+namespace+'/schemas/csv-info/'

# giving file extension
ext = ('.csv')

for f in os.listdir(basePath):
    if f.endswith(ext):
        stemName = Path(basePath).stem
        csvPath = basePath+'/'+f
        print(f)
        with open(csvPath) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            list_of_column_names = []
            for row in csv_reader:
                list_of_column_names.append(row)
            print(list_of_column_names[0])

            outputFile = stemName+'-list.txt'
            f = open(outputFile, "w")
            f.write(str(list_of_column_names[0]))
#            print(list_of_column_names[0])
            f.close()