# Transformers README
This directory contains the data transformation scripts run prior to generating the documentation webpages.

: Source Files: [stadocgen root]/mids/app/data/source/mids-source
: Target Directory: [stadocgen root]/mids/app/data/output

## Contents
1. levels_transformations.py
2. mappings_transformations.py
3. terms_transformations.py


## Basic Workflow
1. Rename and process columns in both the levels and information elements source files
2. Combine levels and information elements > /data/output/mids-termlist.csv
3. Process each mapping file > data/output/[namespace]-mappings.csv

##
1. All files in the source directory are preserved in their original state upon import into stadocgen.
2. Source files are only updated when a more recent version is imported (copied) into StaDocGen. 