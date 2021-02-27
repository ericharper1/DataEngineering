import pandas as pd

census_filename = 'acs2017_census_tract_data-1.csv'
covid_filename = 'COVID_county_data.csv'
print(f"reading file: {census_filename}")
print(f"reading file: {covid_filename}")
census_df = pd.read_csv(census_filename, low_memory=False, parse_dates=['TractId'])
covid_df = pd.read_csv(covid_filename, low_memory=False, parse_dates=['date'])
census_df = census_df.groupby(['State', 'County']).sum()
census_df.to_csv('census_group_by.csv')
census_group_by_filename = 'census_group_by.csv'
covid_df = covid_df.groupby(['state', 'county', 'fips']).sum()
covid_df.to_csv('covid_group_by.csv')
covid_group_by_filename = 'covid_group_by.csv'
print(f"reading file: {census_group_by_filename}")
census_df = pd.read_csv(census_group_by_filename, low_memory=False, parse_dates=['State'])
print(f"reading file: {covid_group_by_filename}")
covid_df = pd.read_csv(covid_group_by_filename, low_memory=False, parse_dates=['state'])

for index, row in census_df.iterrows():
    census_df.at[index, 'County'] = ' '.join(row['County'].split(' ')[:-1])
# print(census_df)
# print(covid_df)

# covid_df.merge()
print(covid_df)
