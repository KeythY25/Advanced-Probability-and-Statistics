import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load your dataset here
# Example: data = pd.read_csv('your_dataset.csv')
csv_file = 'housing.csv'
data = pd.read_csv(csv_file)

# Create a violin plot for 'Population' by 'Ocean Proximity'
plt.figure(figsize=(12, 6))
violin_plot = sns.violinplot(x='ocean_proximity', y='population', data=data, palette='viridis')
plt.title('Violin Plot of Population by Ocean Proximity')
plt.xlabel('Ocean Proximity')
plt.ylabel('Population')
plt.xticks(rotation=45)

# Add median values as annotations
medians = data.groupby('ocean_proximity')['population'].median()
vertical_offset = data['population'].median() * 0.05  # Adjust the offset as needed
for i, median in enumerate(medians):
    violin_plot.text(i, median + vertical_offset, f'{median:.2f}', ha='center', va='bottom', fontsize=10)

plt.show()

# Define a custom color palette for 'Ocean Proximity' categories
custom_colors = ['#FF9999', '#66B2FF', '#99FF99', '#FFCC99', '#c2c2f0']

# Calculate the counts of each 'Ocean Proximity' category
ocean_proximity_counts = data['ocean_proximity'].value_counts()

# C Create a pie chart with custom colors and start at the 12 o'clock position
plt.figure(figsize=(8, 8))
plt.pie(ocean_proximity_counts, labels=ocean_proximity_counts.index, autopct='%1.1f%%', startangle=90, colors=custom_colors, counterclock=False)

plt.title('Pie Chart of Ocean Proximity Distribution')
plt.axis('equal')  # Equal aspect ratio ensures that the pie is drawn as a circle.

plt.show()