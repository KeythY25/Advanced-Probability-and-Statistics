import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
csv_file = "AZ_Pop2020.csv"  # Replace with the path to your CSV file
data = pd.read_csv(csv_file)

df = pd.DataFrame({
    'County' : data['Arizona Counties'],
    'Population' : data['2020'],
    
})

print(df)


# Create a bar graph
plt.figure(figsize=(14, 6))  # Adjust the figure size as needed

plt.bar(df['County'], df['Population'], color='royalblue')
plt.xlabel("County")
plt.ylabel("Population")
plt.title("Arizona Population")

# Rotate the x-axis labels for better readability (optional)
plt.xticks(rotation=90)

# Show the plot
plt.tight_layout
plt.show()

df2 = df.sort_values(by='Population', ascending=True)

plt.figure(figsize=(10,10))
bars = plt.barh(df2['County'], df2['Population'], color='royalblue')
plt.ylabel("County")
plt.xlabel('Population in 2020')
plt.title('Arizona Population 2020')

for bar, population in zip(bars, df2['Population']):
    plt.text(bar.get_width(), bar.get_y() + bar.get_height() / 2, f'{population:,}', ha='left', va='center')

plt.tight_layout()
plt.show()