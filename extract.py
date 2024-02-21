# import packages pandas and numpy
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings("ignore", "\nPyarrow", DeprecationWarning)

# function to extract excel file as dataframe
def extract(file_path, sheet, rows, ind_col):
    
    # read the file into memory
    data = pd.read_excel(file_path, sheet_name = sheet, nrows = rows, index_col = ind_col)

    # excel to df
    data = pd.DataFrame(data)
    
    # printing details about the file
    print(f"data store in [{file_path}]:")
    print(f"\nNumber of rows [{data.shape[0]}], and Number of columns [{data.shape[1]}] in dataframe")
    print(f"\nColumns in dataframe with it's data types: ")
    
    # print data types
    print(data.dtypes)
    
    print(f"\n Printing the count value of NULL per column\n")
    print(data.isna().sum())
    
    # print message before returning the dataframe
    print(f"\nTo view the dataframe extracted from {file_path}, display the value returned by this function!\n\n") 
    
    return data

# call the function
psgc = extract("datasets\PSGC-4Q-2023-Publication-Datafile.xlsx",
               sheet = 3,
               rows = None,
               ind_col = None )

# renaming and cleaning the columns/headers 
def transform(data):
    
    # changing columns/headers string to lowercase, replacing special characters to spaces
    clean_columns = data.columns.str.lower().str.replace('\W', '').str.replace('-', '').str.replace('\n', '').str.replace(':', '').str.replace('/', '').str.replace(' ', '')
    
    # passing function as clean_columns to dataframe columns
    data.columns = clean_columns
    
    # return to function
    return data

# column names not transformed
psgc.columns

# Transformation
psgc = transform(psgc)

print(psgc.columns)

