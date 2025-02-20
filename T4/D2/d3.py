import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load data from CSV file
csv_file = 'income.csv'
data = pd.read_csv(csv_file)

# Define age intervals in 10-year intervals
age_intervals = pd.cut(data['age'], bins=range(0, 101, 10), right=False)

# Create a dataframe
df = pd.DataFrame({
    'Age Intervals': age_intervals,
    'Income': data['fnlwgt'] / 1_000_000,
    'Education': data['education.num'],
    'Race': data['race'],
    'Sex': data['sex']
})

# Use Seaborn's pairplot to visualize relationships, coloring by 'Sex' and 'Race'
sns.pairplot(df, hue='Age Intervals', palette='viridis', diag_kind='kde')
plt.suptitle('Pairplot of Age, Education, Race, and Income by Age Intervals')
plt.show()
