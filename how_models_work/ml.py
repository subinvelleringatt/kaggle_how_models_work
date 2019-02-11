import pandas as pd
melbourne_file_path = 'C:\\Users\\sinsbv\\Desktop\\Project\\Kaggle\\Tutorial\\how_models_work\\melb_data.csv'
melbourne_file_path
# read the data and store data in DataFrame titled melbourne_data
melbourne_data = pd.read_csv(melbourne_file_path)
# print a summary of the data in Melbourne data
melbourne_data.describe()
from learntools.core import binder
