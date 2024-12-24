# Metaschemas - Metadata Scheme Documentation
TDWG standards documentation are built using a set of CSV metadata files as the primary data source for generating dyanmic content at runtime. Defined as part of the TDWG Standards Specification, the same set of CSV files are used to generate RDF using the rs.tdwg.org toolkit. 

Before the CSV metadata files are rendered on a webpage, they must be transformed into a format more suitable for the web using a small set of transformation python scripts. As a result, each StaDocGen instance contains both the original and transformed csv metadata files.  The purpose of this application is to generate a human-readable version of both sets of CSV metadata files. Table schema is a specification defined alongside the [Data Package]() and [Data Resource](https://specs.frictionlessdata.io/data-resource/) specifications as part of the [Frictionless Data Project](https://frictionlessdata.io/). 



## Schemas
Schemas are generated using the tableschemas and csvkit python libraries in the respective standard flask app. The resulting schema files are migrated to this app for separate publication. The tabulated summary below lists the standards with published schemas with a set of informative attributes such as source.


## Definitions
* Table Schema: Table Schema is a simple language- and implementation-agnostic way to declare a schema for tabular data. [https://specs.frictionlessdata.io/table-schema/#language](https://specs.frictionlessdata.io/table-schema/#language)


## Resources
* Table Schema Specification: [https://specs.frictionlessdata.io/table-schema/](https://specs.frictionlessdata.io/table-schema/)
* Frictionless Data: [https://frictionlessdata.io/introduction/](https://frictionlessdata.io/introduction/)


| File | Standard | Namespace | Source | Date Last Modified |
| -- | -- | -- | -- | -- |
| 


## Instances
Published schemas are partitioned by standard and organized accordingly in the project code base.
