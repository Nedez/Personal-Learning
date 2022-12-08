# %%
import numpy as np
import pandas as pd

from pandas import Series, DataFrame

#%%
Series_obj = Series(np.arange(8), index=['row 1', 'row 2', 'row 3', 'row 4', 'row 5', 'row 6', 'row 7', 'row 8' ])
Series_obj

# %% 
# Create a Data Frame object by generating series of 36 random numbers
np.random.seed(25)
DF = DataFrame(
    np.random.rand(36).reshape((6,6)),
    index=['row 1', 'row 2', 'row 3', 'row 4', 'row 5', 'row 6'],
    columns=['column 1', 'column 2', 'column 3', 'column 4', 'column 5', 'column 6']
    )
DF

# %% 
# .loc selects and retrieves specific rows and column in a DataFrame
DF.loc[['row 2', 'row 5'], ['column 5', 'column 2']]

# %%
""" Data Slicing uses index values to select and return 
a slice of several values from a dataset. It will return
the values between two index points seperated by ":" """ 

Series_obj['row 3': 'row 7']

# %%
