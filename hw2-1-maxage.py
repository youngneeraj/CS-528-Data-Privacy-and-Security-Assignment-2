import pandas as pd

# Replace 'your_file_path' with the path to your dataset file.
filepath = r"C:\Users\neera\Downloads\adult\adult.data"
column_names = [
    'age', 'workclass', 'fnlwgt', 'education', 'education_num',
    'marital_status', 'occupation', 'relationship', 'race', 'sex',
    'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'income'
]

data = pd.read_csv(filepath, header=None, names=column_names)
max_age = data['age'].max()
print(max_age)
