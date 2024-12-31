import csv
from config import get_project_root
import pandas as pd
import urllib.request
import shutil

root = get_project_root()

# Mapping source files are stored as *.tsv (tab-delimited). StaDocGen parses CSV when generating documentation. This script converts the source tsv to source csv.
# Files:
dwc_filestem = 'sssom_mids_dwc_biology_02'
dwc_repofile = 'https://raw.githubusercontent.com/tdwg/mids/refs/heads/main/sssom-mapping/dwc/biology/sssom_mids_dwc_biology_02.sssom.tsv'
dwc_localtsv = str(root) + '/mids/app/data/source/mids-repo/mappings/' + dwc_filestem + '.tsv'
dwc_localcsv = str(root) + '/mids/app/data/source/mids-repo/mappings/' + dwc_filestem + '.csv'
dwc_sssomfile = str(root) + '/mids/app/data/output/mids-dwc-sssom.csv'
dwc_uniquecsv = str(root) + '/mids/app/data/source/mids-repo/mappings/dwc_unique_class_property_pairs.csv'

abcd_filestem = 'sssom_mids_abcd_biology_02'
abcd_repofile = 'https://raw.githubusercontent.com/tdwg/mids/refs/heads/main/sssom-mapping/abcd/biology/sssom_mids_abcd_biology_02.sssom.tsv'
abcd_localtsv = str(root) + '/mids/app/data/source/mids-repo/mappings/' + abcd_filestem + '.tsv'
abcd_localcsv = str(root) + '/mids/app/data/source/mids-repo/mappings/' + abcd_filestem + '.csv'
abcd_sssomfile = str(root) + '/mids/app/data/output/mids-abcd-sssom.csv'
abcd_uniquecsv = str(root) + '/mids/app/data/source/mids-repo/mappings/abcd_unique_class_property_pairs.csv'

def download(url, localfile):
    urllib.request.urlretrieve(url, localfile)

def convert_tsv_to_csv(source, target):
    with open(source, 'r') as tsvfile:
        reader = csv.reader(tsvfile, delimiter='\t')
        with open(target, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for row in reader:
                if row:
                    writer.writerow(row)

# Download both Mapping Files
download(dwc_repofile, dwc_localtsv)
download(abcd_repofile, abcd_localtsv)

# Convert Files
convert_tsv_to_csv(dwc_localtsv, dwc_localcsv)
convert_tsv_to_csv(abcd_localtsv, abcd_localcsv)

# ------------------------------------------------------------
# DWC

df_dwc = pd.read_csv(dwc_localcsv, encoding="utf8")

# Generate Unique Class-Property Pairs for DWC
df_dwc_mapping = df_dwc[['sssom:subject_category','sssom:subject_id']].drop_duplicates()
df_dwc_mapping.rename(columns={'sssom:subject_id': 'qualified_term',
                    'sssom:subject_category': 'class_name'
                   }, inplace=True)
df_dwc_mapping['term_local_name'] = df_dwc_mapping['qualified_term'].str.replace('mids:', '')
df_dwc_mapping.to_csv(dwc_uniquecsv, index=False, encoding='utf8')

# Write new mappings file
df_dwc['object_source_version'] = 'http://rs.tdwg.org/dwc/terms'
# Replace colon in column names with underscores - jinja2 template reserved character
df_dwc.columns = df_dwc.columns.str.replace(':','_', regex=True)
df_dwc.to_csv(dwc_sssomfile, index=False, encoding='utf8')

# ------------------------------------------------------------
# ABCD

df_abcd = pd.read_csv(abcd_localcsv, encoding="utf8")
# Generate Unique Class-Property Pairs for ABCD
df_abcd_mapping = df_abcd[['sssom:subject_category','sssom:subject_id']].drop_duplicates()
df_abcd_mapping.rename(columns={'sssom:subject_id': 'qualified_term',
                    'sssom:subject_category': 'class_name'
                   }, inplace=True)
df_abcd_mapping['term_local_name'] = df_abcd_mapping['qualified_term'].str.replace('mids:', '')
df_abcd_mapping.to_csv(abcd_uniquecsv, index=False, encoding='utf8')

# Write new mappings file
df_abcd['object_source_version'] = 'http://www.tdwg.org/schemas/abcd/2.06'
# Replace colon in column names with underscores - jinja2 template reserved character
df_abcd.columns = df_abcd.columns.str.replace(':','_', regex=True)
df_abcd.to_csv(abcd_sssomfile, index=False, encoding='utf8')


# Create copies of both mappings files in output directory
#shutil.copy(dwc_localcsv, dwc_sssomfile)
#shutil.copy(abcd_localcsv, abcd_sssomfile)