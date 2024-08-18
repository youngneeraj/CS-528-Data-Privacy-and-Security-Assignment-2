import pandas as pd
import numpy as np

def load_data_and_calculate_frequencies(filepath):
    """Loads the dataset and calculates frequencies of each 'Education' level."""
    columns = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 
               'marital_status', 'occupation', 'relationship', 'race', 
               'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 
               'native_country', 'income']
    data = pd.read_csv(filepath, header=None, names=columns, skipinitialspace=True)
    education_frequencies = data['education'].value_counts()
    return education_frequencies

def apply_exponential_mechanism_corrected(frequencies, epsilon):
    """Corrected approach to apply the exponential mechanism with adjusted utilities."""
    max_utility = frequencies.max()
    utilities = frequencies.apply(lambda x: x - max_utility)  # Adjusted utilities

    # Scale utilities to mitigate exponential skew
    scaled_utilities = utilities / utilities.abs().max() * 10  # Example scaling factor

    probabilities = np.exp(epsilon * scaled_utilities / 2.0)
    probabilities /= probabilities.sum()

    choice = np.random.choice(frequencies.index, p=probabilities)
    return choice, probabilities
# Example usage
filepath = r"C:\Users\neera\Downloads\adult\adult.data"
education_frequencies = load_data_and_calculate_frequencies(filepath)

print("Original Education Frequencies:")
print(education_frequencies)
epsilon_values = [0.5, 1.0]
for epsilon in epsilon_values:
    selected, probs = apply_exponential_mechanism_corrected(education_frequencies, epsilon)
    
    print(f"\n=== ε={epsilon} ===")
    print(f"Selected Education Level: {selected}")
    print("\nUtilities after Normalization (Normalized Frequencies):")
   
    print("\nProbabilities:")
    print(f"\n=== ε={epsilon} ===")
    print(f"Selected Education Level: {selected}")
    print("Probabilities:")
    print(probs)
   