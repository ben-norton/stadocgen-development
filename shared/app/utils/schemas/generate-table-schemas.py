from tableschema import Table, infer, Schema
from json_extract import GetValue2
import glob
import csv
import json
import os
from datetime import date
from pathlib import Path

today = date.today()
ts = today.strftime("%Y%m%d")

# Paths
currentPath = Path().absolute()
projectPath = currentPath.parent.parent.parent

# Source Files Path
sourcePath = str(projectPath) + '/app/data/source-files/mids-repo/'

# Timestamped output path
targetPath = str(currentPath) + '/tableschemas/'+str(ts)

# Create output path if it doesn't exist
if not os.path.isdir(targetPath):
    os.mkdir(targetPath)

# giving file extension
ext = ('.csv')

# iterating over all files
#folders = os.listdir(sourcePath)

sourceFiles = str(sourcePath) + "*.csv"
for f in glob.glob(sourceFiles):
    if f.endswith(ext):
        stemName = Path(f).stem
        table = Table(f)

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
        outputSchema = os.path.join(f, targetPath + '/' + stemName + "-schema.json")
        columnsSchema = os.path.join(f, targetPath + '/' + stemName + "-columns.json")
        templateCsv = os.path.join(f, targetPath + '/' + stemName + "-template.csv")

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
