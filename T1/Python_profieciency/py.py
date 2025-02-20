# Import Library
import pandas as pd

# Read file using panda
data = pd.read_csv('exercise_data.csv')

# Group the data by Exercise Group
grouped = data.groupby('Exercise Group')

# Calculate the total blood pressure reduction for each group
# This sums up the post BP for each group and subract from th sum of pre BP for each group
total_reduction = grouped['Post-exercise Systolic BP'].sum() - grouped['Pre-exercise Systolic BP'].sum() 

# Print the total blood pressure reduction
print("Total Blood Pressure Reduction:")
print(total_reduction)
