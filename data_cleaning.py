import pandas as pd
import streamlit as st

st.set_page_config(layout='wide')
df=pd.read_excel(r"C:\Users\steph\Desktop\Power BI datasets\Power BI - Final Project.xlsx")

# st.title("Data cleaning")

# for i, col in enumerate(df.columns):
#     st.info(f"{i+1}. {col}")

def replace_sql(row):
    if 'sql' in row.lower():
        return 'SQL'
    return row


df_copy = df.copy()
df_copy['Q5 - Favorite Programming Language'] = df_copy['Q5 - Favorite Programming Language'].str.replace('^.*sql.*$', "SQL", regex=True, case=False)
# df_copy['Q5 - Favorite Programming Language'] = df_copy['Q5 - Favorite Programming Language'].apply(func=replace_sql)

df_copy['Q5 - Favorite Programming Language'] = df_copy['Q5 - Favorite Programming Language'].str.replace('^.*other.*$', "Others", regex=True, case=False)

# c1, c2 = st.columns((5, 5))
# with c1:
#     st.write(df['Q5 - Favorite Programming Language'].sample(50, random_state=24))
#
# with c2:
#     st.write(df_copy['Q5 - Favorite Programming Language'].sample(50, random_state=24))


df_copy.to_excel(r"C:\Users\steph\Desktop\Power BI datasets\Project semi-cleaned.xlsx")
