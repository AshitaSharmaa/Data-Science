import pandas as pd
df = pd.read_csv('salaries_by_college_major.csv')
#to see column names
print(df.columns)
#to check for 'Not Available' values in data
# print(df.isna())
# print(df.tail())
#to delete the records where data is not available
clean_df = df.dropna()

## which degree has the highest starting salary ##

max_index = clean_df['Starting Median Salary'].idxmax()
print(clean_df['Undergraduate Major'][max_index])
print(clean_df['Starting Median Salary'].max())


## What college major has the highest mid-career salary? How much do graduates with this major earn? (Mid-career is defined as having 10+ years of experience). ##

max_index = clean_df['Mid-Career Median Salary'].idxmax()
print(clean_df['Undergraduate Major'][max_index])
print(clean_df['Mid-Career Median Salary'].max())

## Which college major has the lowest starting salary and how much do graduates earn after university? ##

min_index = clean_df['Starting Median Salary'].idxmin()
print(clean_df['Undergraduate Major'][min_index])
print(clean_df['Starting Median Salary'].min())

## Which college major has the lowest mid-career salary and how much can people expect to earn with this degree? ##

min_index = clean_df['Mid-Career Median Salary'].idxmin()
print(clean_df['Undergraduate Major'][min_index])
print(clean_df['Mid-Career Median Salary'].min())

##Lowest Risk Majors: the majors which have the least difference b/w 90th percentile and 10th percentile##

diff = clean_df['Mid-Career 90th Percentile Salary'].subtract(clean_df['Mid-Career 10th Percentile Salary'])

#Insert this dataframe into existing dataframe

clean_df.insert(1, 'spread', diff)
low_risk_majors = clean_df.sort_values(by=['spread'])
print(low_risk_majors[['Undergraduate Major','spread']].head())

##degrees with the highest potential##

highest_pot_majors = clean_df.sort_values(by=['Mid-Career 90th Percentile Salary'], ascending=False)
print(highest_pot_majors[['Undergraduate Major','Mid-Career 90th Percentile Salary']].head())

##Degrees with the greatest spread in salaries##

greatest_spread_majors = clean_df.sort_values(by=['spread'], ascending=False)
print(greatest_spread_majors[['Undergraduate Major','spread']].head())

## which category of degrees has the highest average salary? Is it STEM, Business or HASS (Humanities, Arts, and Social Science)?

# pd.options.display.float_format = '{:,.2f}'.format
print(clean_df.groupby('Group').count())
pd.options.display.float_format = '{:,.2f}'.format
print(clean_df.groupby('Group').mean('Mid-Career 90th Percentile Salary'))
