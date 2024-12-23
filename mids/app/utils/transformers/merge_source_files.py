import pandas as pd
from datetime import date
from pathlib import Path
import csv
import os

today = date.today()
ts = today.strftime("%Y%m%d")

# Paths
currentPath = Path().absolute()
projectPath = currentPath.parent.parent.parent

# Source Files Path
levelsFile = str(projectPath) + '/app/data/output/mids-levels.csv'
infoElFile = str(projectPath) + '/app/data/output/mids-information-elements.csv'
termsFile = str(projectPath) + '/app/data/output/mids-termlist.csv'

# Create empty template if file doesn't exist
if not os.path.isdir(termsFile):
    fields = ['namespace','term_local_name','label','definition','usage','notes','examples','rdf_type','class_name','is_required','is_repeatable','term_created','term_modified','compound_name','namespace_iri','term_iri','term_ns_name','term_version_iri','datatype','purpose','editorial_note','alt_label']
    with open(termsFile, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames = fields)
        writer.writeheader()


df_levels = pd.read_csv(levelsFile, encoding="utf8")
df_infoElements = pd.read_csv(infoElFile, encoding="utf8")
df_terms = pd.read_csv(termsFile, encoding="utf8")

mergeFrames = [df_levels, df_infoElements]

df_terms = pd.concat([df_terms,df_levels])
df_final = pd.concat([df_terms,df_infoElements])

## Save
df_final.to_csv(termsFile, index=False, encoding='utf8')