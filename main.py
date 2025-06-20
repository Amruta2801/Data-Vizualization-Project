import numpy as np
import pandas as pd

# Set seed for reproducibility
np.random.seed(0)

# Create a sample population of 100 people
population_size = 100
genders = np.random.choice(['Male', 'Female', 'Non-binary'], size=population_size, p=[0.45, 0.45, 0.1])
ages = np.random.normal(loc=35, scale=10, size=population_size).astype(int)

# Create a DataFrame
df = pd.DataFrame({
    'Gender': genders,
    'Age': ages
})

# Display the first 5 rows
print(df.head())


import matplotlib.pyplot as plt

# Count how many people are in each gender category
gender_counts = df['Gender'].value_counts()

# Plotting the bar chart
plt.figure(figsize=(6, 4))
plt.bar(gender_counts.index, gender_counts.values, color='skyblue')
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.tight_layout()
plt.show()


# Plotting the histogram
plt.figure(figsize=(6, 4))
plt.hist(df['Age'], bins=10, color='salmon', edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()
