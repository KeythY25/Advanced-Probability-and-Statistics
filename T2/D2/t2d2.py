import numpy as np
from scipy import stats
import pandas as pd


data = pd.read_csv('grade.csv')
df = pd.DataFrame(data)

z_scores = stats.zscore(df['Grade'])
df['Z Score'] = z_scores

grades = np.array(df['Grade'])
median = np.median(data)
mean = np.mean(data)

print(df)
print(f'Mean: {mean}')
print(f'Median: {median}')






