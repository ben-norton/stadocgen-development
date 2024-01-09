import pandas as pd
from io import StringIO
from pandas_schema import Column, Schema
from pandas_schema.validation import LeadingWhitespaceValidation, TrailingWhitespaceValidation, CanConvertValidation, MatchesPatternValidation, InRangeValidation, InListValidation

schema = Schema([
    Column('Given Name', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('Family Name', [LeadingWhitespaceValidation(), TrailingWhitespaceValidation()]),
    Column('Age', [InRangeValidation(0, 120)]),
    Column('Sex', [InListValidation(['Male', 'Female', 'Other'])]),
    Column('Customer ID', [MatchesPatternValidation(r'\d{4}[A-Z]{4}')])
])
