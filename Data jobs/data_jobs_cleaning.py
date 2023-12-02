import pandas as pd

#Initialize data
pd.set_option("display.max_columns", 12)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

df = pd.read_csv(r"C:\Users\steph\Desktop\Excel-CSV files\Practice for Pandas\DS dataset\ds_salaries.csv")
df.drop_duplicates(inplace=True)

#Data Science
# df['job_title'] = df['job_title'].str.replace('^.*data scien.*$', "Data Scientist", regex=True, case=False)
df['job_title'] = df['job_title'].where(~df['job_title'].str.contains(r'.*data sci|head of data.*', regex=True, case=False), 'Data Scientist')

#Data anaylist
df['job_title'] = df['job_title'].where(~df['job_title'].str.contains(r'.*data anal|Analytics Engineer|Data Specialist.*',
                                                                      regex=True, case=False), 'Data Analyst')

#Data Engineer
df['job_title'] = df['job_title'].where(~df['job_title'].str.contains(r'.*data engi.*',
                                                                      regex=True, case=False), 'Data Engineer')

#Machine Learning Specialist
df['job_title'] = df['job_title'].where(~df['job_title'].str.contains(r'.*Machine|AI|ML.*', regex=True, case=False), 'ML Specialist')

#Format other data jobs
df['job_title'] = df.job_title.apply(lambda x: "Others" if x not in ['Data Scientist', 'Data Analyst', 'Data Engineer',
                                                                     'ML Specialist'] else x)

#Check distance
# print(df[['employee_residence', 'company_location']].head(10))

#Using zip function to compare 2 features
df['Close Proximity'] = ['Yes' if i == j else 'No' for i, j in zip(df['employee_residence'], df['company_location'])]

df.drop(['employee_residence', 'company_location'], axis=1, inplace=True)

#Engineering Remote ratio
df['remote_ratio'] = df['remote_ratio'].replace({100: 3, 50: 2, 0: 1})

#Dealing with values in columns that appear less than a certain threshold
counts = df['job_title'].value_counts()
mask = df['job_title'].isin(counts[counts<80].index)
print(counts)

print(df.sample(20))
