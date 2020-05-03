# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')

#Independent variables that has to be pushed separately
X = dataset.iloc[:,:-1].values

# Dependent variables separately accumulated
Y = dataset.iloc[:,3].values