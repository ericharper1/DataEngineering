import pandas as pd
import numpy as np
import decimal
import matplotlib.pyplot as plt
import re

log_filename = 'crash_data.csv'
print(f"reading file: {log_filename}")
df = pd.read_csv(log_filename, low_memory=False, parse_dates=['Crash ID'])

# Existence assertions
null_crash_id = df['Crash ID'].isnull().values.any()
null_participant_id = df['Participant ID'].isnull().values.any()
record_type_column = df['Record Type']
record_type_range = range(int(record_type_column.min()), int(record_type_column.max() + 1))
year_column = df['Crash Year']
year_range = range(2019, 2019 + 1)
month_column = df['Crash Month']
month_range = range(1, 12 + 1)
day_column = df['Crash Day']
day_range = range(1, 31 + 1)
record_type_out_of_range = record_type_column.values.any() in record_type_range
year_out_of_range = year_column.values.any() in year_range
month_out_of_range = month_column.values.any() in month_range
day_out_of_range = day_column.values.any() in day_range

print("Crash ID violations: {}".format(null_crash_id))
print("Participant ID violations: {}".format(null_participant_id))
print("Record Type is out of range: {}".format(record_type_out_of_range))
if year_out_of_range or month_out_of_range or day_out_of_range:
    print("Date is out of range: True")


