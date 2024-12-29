# Source File Specifications

File: MIDS-levels-draft.csv
CSV file contains MIDS levels that are considered semantically equivalent to class in the common class-property RDF structure.

| source column name | qualified term                   | target column name | remarks                                                                   |
| -- |----------------------------------|--------------------|---------------------------------------------------------------------------|
| level | skos:hiddenLabel                 | class_name         | MIDS Levels are equivalent to class in a the class-property RDF structure |
| prefLabel | skos:prefLabel                   | class_label        |
| shortDescription | schema:disambiguatingDescription | short_description  |
| longDescription | dcterms:abstract                 | abstract           |
| purpose |                                  | purpose            | Defined here as the intention or objective of a term                      |

## Merged File Fields


## Mappings to TDWG fields
level > term_local_name
level > term_local_name
prefLabel > label
shortDescription > definition
longDescription > notes

## Processing Notes
MIDS-levels-draft.csv
1. Add column rdf_type
2. Set all rdf_type values http://www.w3.org/2000/01/rdf-schema#Class
3. Change column names:
    level > term_local_name
    prefLabel > label
    shortDescription > definition
    longDescription > notes
  
mids_information_elements_draft.csv
1. Set rdf_type to http://www.w3.org/1999/02/22-rdf-syntax-ns#Property
2. Column name changes 
   informationElement_localName > term_local_name
   usage > purpose
   recommendations > usage_note
   tdwgutility_required > is_required
   tdwgutility_repeatable > is_repeatable
   term_status >editorial_note
3. Update boolean
4. Add scope_note
5. Populate scope_note with value in parentheses in is_required
6. Delete term_modified, term_added - Needs to reflect ratification date in this context

## Merged File Fields
namespace
term_local_name
label
definition
usage
notes
examples
rdf_type
class_name
is_required
is_repeatable
term_created
term_modified
compound_name
namespace_iri
term_iri
term_ns_name
term_version_iri
datatype
purpose
scope_note
usage_note
editorial_note