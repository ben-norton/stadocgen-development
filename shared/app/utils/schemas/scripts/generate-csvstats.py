import csvkit
from datetime import date
from pathlib import Path
import os

today = date.today()
ts = today.strftime("%Y%m%d")
namespace = 'mids'
current_dir = Path().absolute()
path = current_dir.parent.parent
csvPath = str(path)+'/utils/sources/'+namespace+'/'+namespace+'-source'
tsPath = str(path)+'/utils/schemas/'+namespace+'/schemas/csvstats/'+str(ts)

if not os.path.isdir(tsPath):
    os.mkdir(tsPath)

ext = ('.csv')

# iterating over all files
for f in os.listdir(csvPath):
    if f.endswith(ext):
        destFile = os.path.splitext(f)[0] + "-stats.csv"
        dest = str(tsPath) + '/' + destFile
        fp = csvPath + '/' + f
        os.system("csvstat " + fp + " > " + dest)
