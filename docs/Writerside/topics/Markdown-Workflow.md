# Workflows

Current TDWG procedures include the submission of a standardized set of CSV files for the purposes of generate RDF code and permanent and resolvable URIs for TDWG terms. 
The goal of Stadocgen is to automatically generate standardized documentation webpages using the same set of CSV files currently used for RDF. used that same set of CSV files to generate a standardized documentation webpages for TDWG standard. 
The instructions and specifications below are based on the Latimer Core standard

2 Sets of Files
1. CSV Vocabulary Files
2. Markdown files containing website content



# Latimer Core
Stadocgen was developed during the review of Latimer Core to generate documentation. LtC was the excellent test case due to its 
size, complexity, and relationships with several pre-existing standards.


Source Repo: https://github.com/tdwg/ltc
Source CSV Files: 
[repo]\source\terms\
    abcd.csv
    chrono.csv
    dcterms.csv
    dwc.csv
    ltc.csv
    ltc_categories.csv
    ltc_datatypes.csv
    ltc_terms_source.csv
    schema.csv
    mapping\
        ltc_skos_mapping.csv
        ltc_sssom_mapping.csv


## Transformations
Transformation scripts
After local CSV and markdown files have been refreshed from source repository, run the following transformations scripts
app/utils/transformations/terms_transformations.py
app/utils/transformations/ltc-paths.py
app/utils/transformations/skos-transformations.py
app/utils/transformations/sssom-transformations.py