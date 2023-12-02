import pandas as pd
from category_encoders import TargetEncoder
import os

#Initialize data
pd.set_option("display.max_columns", None)
pd.set_option('display.float_format', lambda x: '%.3f' % x)

df = pd.read_csv(r"https://raw.githubusercontent.com/DarynBang/Testfile/main/Data%20jobs/ds_salaries.csv")
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

#Engineering Remote ratio
df['remote_ratio'] = df['remote_ratio'].replace({100: 3, 50: 2, 0: 1})


#Save file as csv file
df.to_csv(os.getcwd() +'/cleaned_Data.csv')
