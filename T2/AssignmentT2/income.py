
import pandas as pd
import matplotlib.pyplot as plt

# Load the income dataset from a CSV file
income_data = pd.read_csv('incomedata.csv')

# Create a DataFrame
income_df = pd.DataFrame({
    'Age': income_data['age'],
    'Income': income_data['fnlwgt'],  
    'Education': income_data['education'],
    'Marital Status': income_data['marital-status'],
    'Gender': income_data['gender'],
    'Race': income_data['race'],
    'Hours Worked/Week': income_data['hours-per-week']
})

# Define the categorical variable
categorical_variable = 'Gender'

# Group the data by the categorical variable
grouped_data = income_df.groupby(categorical_variable)

# Calculate measures of central tendency and variability for 'Income' in each group
summary_stats = grouped_data['Income'].agg(['mean', 'median', 'var', 'std'])

# Print the summary statistics
print(summary_stats)

# Show box plot for male
male_data = income_df[income_df['Gender'] == 'Male']
plt.figure(figsize=(8, 6))
plt.boxplot(male_data['Income'], vert=False)
plt.title('Income Distribution for Male')
plt.xlabel('Income')

# Show box plot for Female
female_data = income_df[income_df['Gender'] == 'Female']
plt.figure(figsize=(8, 6))
plt.boxplot(female_data['Income'], vert=False)
plt.title('Income Distribution for Female')
plt.xlabel('Income')
plt.show()
