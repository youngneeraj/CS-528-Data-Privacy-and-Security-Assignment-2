import pandas as pd

def calculate_global_sensitivity(filepath, max_possible_age=90, min_age_considered=26):
    # Load the dataset
    column_names = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 
                    'marital_status', 'occupation', 'relationship', 'race', 'sex', 
                    'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'income']
    data = pd.read_csv(filepath, names=column_names, header=None, skipinitialspace=True)

    # Filter the dataset for age > 25
    filtered_data = data[data['age'] > 25]

    # Calculate the number of records after filtering
    n = filtered_data.shape[0]

    # Calculate and return the global sensitivity
    return (max_possible_age - min_age_considered) / n

# Example usage
filepath = r"C:\Users\neera\Downloads\adult\adult.data"
global_sensitivity = calculate_global_sensitivity(filepath)
print(f"Global sensitivity: {global_sensitivity}")
