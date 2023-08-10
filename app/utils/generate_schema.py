from tableschema import Table, infer, Schema
from json_extract import extract_values
import pandas as pd
import json
import os
import argparse
from pathlib import Path

# python generate_schema.py _csv data\ltc\ltc_set\ltc_terms_list.csv _o ltc_terms_list
# python generate_schema.py _csv data\ltc\ltc_source\ltc_terms_source.csv _o ltc_terms_source
# python generate_schema.py _csv data\ltc\ltc_source\ltc_terms_source.csv _o ltc_terms_source
# python generate_schema.py -csv data\ltc\ltc-source\ltc_datatypes.csv -o ltc-datatypes
#python generate-schema.py -csv data\ltc\ltc-docs\ltc-terms-list.csv -o ltc-terms-list


# python generate-schema.py -csv data\ltc\ltc-set\ltc-terms-list.csv -o ltc-terms-list
p = Path(os.path.dirname(__file__))
path = p.parent

parser = argparse.ArgumentParser(description='CSV with Path ')
parser.add_argument('-csv', '--csvPath', help='CSV Path', required=True)
parser.add_argument('-o', '--output', help='Output Filename', required=True)
args = parser.parse_args()
csvfile = args.csvPath
outputFile = args.output
csv = path / csvfile
print(csv)

table = Table(csv)
table.infer(limit=500, confidence=0.55)
schema = table.schema.descriptor
names = extract_values(schema, 'name')
datatypes = extract_values(schema, 'type')
schema_dict = {val: idx for idx, val in enumerate(names)}

#schema_dict = dict(zip(names,datatypes))

schema_json = json.dumps(schema_dict, indent=4)
with open(outputFile + "-columns.json", "w") as outfile:
    outfile.write(schema_json)
table.schema.save(outputFile + '-schema.json')

