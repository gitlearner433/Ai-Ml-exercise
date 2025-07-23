# Databricks notebook source
import pandas as pd
import numpy

# COMMAND ----------

csv_url = 'https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/04_Apply/Students_Alcohol_Consumption/student-mat.csv'
df = pd.read_csv(csv_url)
df.head()

# COMMAND ----------

 stud_alcoh = df.loc[: , "school":"guardian"]
 stud_alcoh.head()

# COMMAND ----------

capitalizer = lambda x: x.capitalize()

# COMMAND ----------

stud_alcoh['Mjob'].apply(capitalizer)
stud_alcoh['Fjob'].apply(capitalizer)

# COMMAND ----------

