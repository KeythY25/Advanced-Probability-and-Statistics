
# Import Libraries
import pandas as pd
import matplotlib.pyplot as plt 
import matplotlib.dates as mdates

# Use panda to import time_data files
data = pd.read_csv('time_data.csv')
# Create a data frame from data
df = pd.DataFrame(data)
# The column data is setup to actual datetime
data['Time'] = pd.to_datetime(data['Time'])
# sort data by time
data = data.sort_values(by='Time')

# Create a scatter plot
data.plot(kind='scatter', x ='Time', y='Throughput')

# Set up to have hour intervals
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=1))
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))

# Set up to have a whole number interval
plt.ylim(0, data['Throughput'].max() + 1)
# Rotate the x-axis labels for better readibility
plt.xticks(rotation = 45)

# Print the data as columns
print((data.to_string()))

# Show the scatter plot
plt.show()
