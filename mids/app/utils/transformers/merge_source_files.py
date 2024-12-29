import pandas as pd
from datetime import date
from pathlib import Path
import csv
import os
from config import get_project_root

today = date.today()
ts = today.strftime("%Y%m%d")

# Paths
currentPath = Path().absolute()
projectPath = currentPath.parent.parent.parent

# Source Files Path
levelsFile = str(projectPath) + '/app/data/output/mids-levels.csv'
infoElFile = str(projectPath) + '/app/data/output/mids-information-elements.csv'
termsFile = str(projectPath) + '/app/data/output/mids-termlist.csv'
mapFile = str(projectPath) + '/app/data/source/mids-schema-maps/mids_class_property_map.csv'

# Create empty template if file doesn't exist
if not os.path.isdir(termsFile):
    fields = ['namespace','term_local_name','label','definition','usage','notes','examples','rdf_type','is_required','is_repeatable','term_created','term_modified','compound_name','namespace_iri','term_iri','term_ns_name','term_version_iri','datatype','purpose','editorial_note','alt_label']
    with open(termsFile, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames = fields)
        writer.writeheader()


df_levels = pd.read_csv(levelsFile, encoding="utf8")
df_infoElements = pd.read_csv(infoElFile, encoding="utf8")
df_terms = pd.read_csv(termsFile, encoding="utf8")
df_map = pd.read_csv(mapFile, encoding="utf8")

mergeFrames = [df_levels, df_infoElements]

df_terms = pd.concat([df_terms,df_levels])
df_final = pd.concat([df_terms,df_infoElements])

# Merge with map
mids_df = pd.merge(df_final, df_map[['term_ns_name', 'class_name']], on='term_ns_name', how='left')

## Save
mids_df.to_csv(termsFile, index=False, encoding='utf8')