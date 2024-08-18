import pandas as pd
from numpy.random import laplace

# Load the dataset and preprocess
def load_and_preprocess_dataset(filepath):
    column_names = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 
                    'marital_status', 'occupation', 'relationship', 'race', 'sex', 
                    'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'income']
    data = pd.read_csv(filepath, names=column_names, na_values="?", skipinitialspace=True)
    # Further preprocessing can be added here if needed (e.g., handling other missing values)
    return data[data['age'] > 25]  # Filtering step for specific query

# Calculate the global sensitivity for the average age query
def calculate_global_sensitivity(data, max_possible_age=90, min_age_considered=26):
    n = data.shape[0]  # The number of records after filtering for age > 25
    return (max_possible_age - min_age_considered) / n

# Function to add Laplace noise based on the global sensitivity and epsilon
def add_laplace_noise(query_result, global_sensitivity, epsilon):
    b = global_sensitivity / epsilon  # Scale parameter for the Laplace distribution
    noise = laplace(0, b)  # Generate noise
    return query_result + noise

# Main function
def main():
    filepath = r"C:\Users\neera\Downloads\adult\adult.data"
    epsilon_values = [0.5, 1.0]  # Different privacy levels to explore

    data = load_and_preprocess_dataset(filepath)
    average_age = data['age'].mean()
    n = data.shape[0]  # Total number of individuals over 25 years of age
    global_sensitivity = calculate_global_sensitivity(data)

    print(f"Number of individuals over 25 years old in the dataset: {n}")
    print(f"Original average age: {average_age}")
    for epsilon in epsilon_values:
        noisy_average_age = add_laplace_noise(average_age, global_sensitivity, epsilon)
        b = global_sensitivity / epsilon
        variance = 2 * (b ** 2)  # Calculate variance of the Laplace noise
        print(f"Noisy average age for {epsilon}-differential privacy: {noisy_average_age} (Variance: {variance})")

        # Simple comparison to illustrate the impact
        difference = abs(noisy_average_age - average_age)
        print(f"Difference from original average age for ε={epsilon}: {difference}")

if __name__ == "__main__":
    main()
