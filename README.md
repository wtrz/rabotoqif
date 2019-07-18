# rabotoqif
Rabobank CSV to QIF conversion

Rabobank.nl has the ability to export bank transactions to csv format.
This format is custom and not supported by personal finance software (i.e. Homebank).
This script converts the Rabobank CSV to widely used Qif format.

Usage:
Put the python file and csv file in same directory.
Run command from directory: "python rabo_converter_qif_v2.py"

The script will:
- Read the CSV (the csv should have naming convention: CSV_*.csv)
- Export QIF
- (Optionally) Remove original CSV.
