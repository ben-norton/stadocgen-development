## Configuration Files README
This directory contains configuration files that contain parameters specific to a given project. The parameters govern
the input and output of stadocgen and allow generalized usage without the need to customize stadocgen for each standard.

### Contents
Configurations for each data standard are stored in a pair of files that are defined as follows:
1. YAML - a yaml file containing standardized sets of key-value pairs, many of which are required. The yaml configuration file must adhere to the established template found here **pending**. See the template for additional information
2. CSV - a csv file that lists the source files needed to generate documentation for a given standard. For each record, values are required for every column. Each file is categorized by role using a controlled vocabulary. See *** for details.

Configuration files are associated with a standard using specific naming conventions and rules governing how files are created and stored in the configuration folder.
If the rules and naming conventions are not adhered to, the programmatic automation of stadocgen will fail.

| Entity  | Convention  | Rule | Example(s)        |
|---|---|---|-------------------|
| Folder  | namespace prefix of a standard | Subfolders must be unique which restricts each standard to one folder | ltc/ |
| CSV File  | Namespace prefix + '-source.csv'  | All values are required for each record, values in the type field must adhere to a controlled vocabulary defined **pending**  | ltc-sources.csv   |
| YAML File  | Namespace prefix + '-paramters.yml'  | Yaml must adhere to the template provided with an option to append custom content to the end of the file. Values for required fields must be provided | ltc-paramters.yml |


