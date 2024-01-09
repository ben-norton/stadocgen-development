from tableschema import Table, infer, Schema
import json_extract
import pandas as pd
import json
import os
import argparse
from pathlib import Path

# python generate-csv-schema.py -csv data\ltc\ltc-set\ltc-termlist-list.csv -o ltc-termlist-list
# python generate-csv-schema.py -csv data\ltc\ltc-source\ltc_terms_source.csv -o ltc-termlist-source
# python generate-csv-schema.py -csv data\ltc\ltc-source\ltc_terms_source.csv -o ltc-termlist-source
# python generate-csv-schema.py -csv data\ltc\ltc-source\ltc_datatypes.csv -o ltc-datatypes
#  python generate-csv-schema.py -csv data\ltc\ltc-docs\ltc-termlist-list.csv -o ltc-termlist-list


# python generate-schema.py -csv data\ltc\ltc-set\ltc-termlist-list.csv -o ltc-termlist-list
#p = Path(os.path.dirname(__file__))
#path = p.parent

namespace = 'ltc'
current_dir = Path().absolute()
path = current_dir.parent
defaultPath = str(path)+'/data/ltc/schemas/tableschemas'


parser = argparse.ArgumentParser(description='CSV with Path ')
parser.add_argument('-csv', '--csvPath', help='CSV Path', required=True)
parser.add_argument('-of', '--outputFile', help='Output Filename', required=True)
args = parser.parse_args()
csvfile = args.csvPath
outputFile = args.outputFile
csv = path / csvfile

table = Table(csv)
table.infer(limit=500, confidence=0.55)
schema = table.schema.descriptor
names = json_extract.GetValue2(schema, 'name')
datatypes = json_extract.GetValue2(schema, 'type')
schema_dict = {val: idx for idx, val in enumerate(names)}

#schema_dict = dict(zip(names,datatypes))

schema_json = json.dumps(schema_dict, indent=4)
outputCols = os.path.join(defaultPath, outputFile + "-columns.json")
outputSchema= os.path.join(defaultPath, outputFile + "-schema.json")

with open(outputCols, "w") as outfile:
    outfile.write(schema_json)
table.schema.save(outputSchema)

