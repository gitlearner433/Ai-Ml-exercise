# Databricks notebook source
import pandas as pd
import numpy as np

# COMMAND ----------

 s1 = pd.Series(np.random.randint(1, high=5, size=100, dtype='l'))
 s2 = pd.Series(np.random.randint(1, high=4, size=100, dtype='l'))
 s3 = pd.Series(np.random.randint(10000, high=30001, size=100, dtype='l'))
 print(s1, s2, s3)

# COMMAND ----------

 housemkt = pd.concat([s1, s2, s3], axis=1)
 housemkt.head()

# COMMAND ----------

housemkt.rename(columns = {0: 'bedrs', 1: 'bathrs', 2: 
'price_sqr_meter'}, inplace=True)
housemkt.head()

# COMMAND ----------

 # join concat the values
 bigcolumn = pd.concat([s1, s2, s3], axis=0)
 # it is still a Series, so we need to transform it to a DataFrame
 bigcolumn = bigcolumn.to_frame()

# COMMAND ----------

print(type(bigcolumn))
bigcolumn

# COMMAND ----------

# MAGIC %md
# MAGIC

# COMMAND ----------

len(bigcolumn)

# COMMAND ----------

bigcolumn.reset_index(drop=True, inplace=True)
bigcolumn

# COMMAND ----------

