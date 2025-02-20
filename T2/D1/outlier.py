import pandas as pd
from scipy import stats

data = pd.read_csv('stockchart.csv')

df = pd.DataFrame(data)

z_scores = stats.zscore(df['Price'])

df['Z_Score'] = z_scores

print(df)
