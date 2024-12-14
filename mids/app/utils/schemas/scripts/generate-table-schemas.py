from tableschema import Table, infer, Schema
from json_extract import GetValue2
import csv
import json
import os
from datetime import date
from pathlib import Path
import glob

today = date.today()
ts = today.strftime("%Y%m%d")

# Command Line Arguements
parser = argparse.ArgumentParser(description='Enter Namespace')
parser.add_argument('-ns', '--ns', help='Namespace in lowercasing', required=True)
args = parser.parse_args()
namespace = args.ns

# Paths
current_sourcePath = Path().absolute()
rootpath = current_dir.parent.parent.parent
schemapath = current_dir.parent
# Change to folder of target csv files
sourcePath = str(rootpath)+'/data/source/'+namespace+'-source'
# Timestamped output path
outputPath = str(schemapath)+'/tableschemas/'+str(ts)

# Create output path if it doesn't exist
if not os.path.isdir(outputPath):
    os.mkdir(outputPath)

# giving file extension
ext = ('.csv')

# iterating over all files
#folders = os.listdir(sourcePath)
files = glob.glob('../sources/'+namespace+'/**/*.csv', recursive=True)
for f in files:
    if f.endswith(ext):

        csvPath = f

        stemName = Path(csvPath).stem
        table = Table(csvPath)

        # Scan first 500 rows to determine datatype
        table.infer(limit=500, confidence=0.55)

        # Table Schema
        schema = table.schema.descriptor
        schema_json = json.dumps(schema, indent=4)

        # Column Names
        columns = table.headers

        # Column Schema (Name and Datatype)
        getColumns = GetValue2(schema)
        names = getColumns.get_values('name')
        datatypes = getColumns.get_values('type')
        columns_dict = dict(zip(names, datatypes))
        columns_json = json.dumps(columns_dict, indent=4)

        # Output (File + Path)
        outputSchema = os.path.join(f, outputPath + '/' + stemName + "-schema.json")
        columnsSchema = os.path.join(f, outputPath + '/' + stemName + "-columns.json")
        templateCsv = os.path.join(f, outputPath + '/' + stemName + "-template.csv")

        # Write Tableschema JSON
        with open(outputSchema, "w") as outfile:
            outfile.write(schema_json)
        table.schema.save(outputSchema)

        # Write template csv (blank with column headers only)
        with open(templateCsv, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(columns)

        # Write Column Schema JSON (Name + Datatype)
        with open(columnsSchema, "w") as outfile:
            outfile.write(columns_json)
