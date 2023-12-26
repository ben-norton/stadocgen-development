from tableschema import Table
import glob
import os
import sys
import argparse
from pathlib import Path, PurePath
# Generate Table Schemas for all CSVs in the Path Provided.
# Saves the Schemas to a Subdirectory of the Source called 'schemas'
# Example: python csv-schemas.py -p ..\data\ltc\ltc-docs\

parser = argparse.ArgumentParser(description='Enter Paths')
parser.add_argument('-p', '--path', help='Path to CSV (using backslashes)', required=True)
args = parser.parse_args()
csvpath = args.path

filepaths = csvpath + "\*.csv"
for csv in glob.glob(filepaths):
    fp = os.path.splitext(csv)[0]
    #Create relative path to subdirectory
    pp = PurePath(csv).parent
    path = os.path.join(pp, 'schemas/table-schemas')
    #Get Filename without extension
    f = Path(csv).stem
    #Set new path with new filename
    jsf = path + '/' + f + '-schema.json'

    table = Table(csv)
    table.infer()
    table.schema.descriptor
    table.read(keyed=True)
    table.schema.save(jsf)
