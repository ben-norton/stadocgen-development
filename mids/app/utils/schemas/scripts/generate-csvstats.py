import csvkit
from datetime import date
from pathlib import Path
import os

today = date.today()
ts = today.strftime("%Y%m%d")
namespace = 'mids'
current_dir = Path().absolute()
rootpath = current_dir.parent.parent.parent
schemapath = current_dir.parent

# Change to location of target csv files
csvPath = str(rootpath)+'/data/source/'+namespace+'-source'

# Timestamped output path
outputPath = str(schemapath)+'/csvstats/'+str(ts)

# Create timestamped folder if it doesn't exist
if not os.path.isdir(outputPath):
    os.mkdir(outputPath)

ext = ('.csv')

# iterating over all files
for f in os.listdir(csvPath):
    if f.endswith(ext):
        destFile = os.path.splitext(f)[0] + "-stats.csv"
        dest = str(outputPath) + '/' + destFile
        fp = csvPath + '/' + f
        os.system("csvstat " + fp + " > " + dest)
