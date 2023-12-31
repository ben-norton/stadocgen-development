from tableschema import Table, infer, Schema
import json_extract
import pandas as pd
import json
import os
import argparse
from pathlib import Path

namespace = 'ltc'
current_dir = Path().absolute()
path = current_dir.parent.parent
basePath = str(path)+'/data/'+namespace+'/'+namespace+'-source'
outputPath = str(path)+'/data/'+namespace+'/schemas/tableschemas/'

# giving file extension
ext = ('.csv')

# iterating over all files
for f in os.listdir(basePath):
    if f.endswith(ext):
        csvPath = basePath+'/'+f
        table = Table(csvPath)
        table.infer(limit=500, confidence=0.55)
        schema = table.schema.descriptor
        schema_json = json.dumps(schema, indent=4)
        stemName = Path(csvPath).stem
        outputSchema = os.path.join(f, outputPath + stemName + "-schema.json")

        with open(outputSchema, "w") as outfile:
            outfile.write(schema_json)
        table.schema.save(outputSchema)
