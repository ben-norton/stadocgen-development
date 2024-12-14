# Python Utils
[stadocgen/utils]  
This folder contains a collection of useful transformation and analysis python scripts 

[stadocgen/utils/transformations]  
Scripts that transform source csv files for purposes of web documentation. The source data is stored under data/source and the target output is stored under data/output

[stadocgen/utils/analysis]  
Scripts to analyze the transformation results

[@]

## Workflow
1. Source files are placed in the data/source folder. All source files should be copied from their respective repository. Example: tdwg/ltc
2. Run scripts stored under utils/transformations
3. The output will be stored under data/output. The website generator only uses data stored in the output directory. Therefore, the transformation scripts are required before the documentation pages will show the source data changes.
