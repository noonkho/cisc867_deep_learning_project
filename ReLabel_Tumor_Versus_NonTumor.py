# Imports the Python libraries
import pandas as pd
import numpy as np

# Reads the default sheet of the excel file (.csv)
dataframe = pd.read_csv("train.csv")

# For the column called 'segmentation', we will re-label the data:
# 1. For all rows that have no values, we will change it to a value '0'
# 2. For all rows that do have values, we will change it to a value '1'

# 1. Indicates Non-Tumor 
dataframe['segmentation'] = dataframe['segmentation'].replace(np.nan,0)

# 2. Indicates Tumor
dataframe['segmentation'] = dataframe['segmentation'].where(dataframe['segmentation'] == 0, 1)

# Exports the dataframe to a new excel file (.csv)
dataframe.to_csv("tumor_vs_nontumor.csv", index=False)
