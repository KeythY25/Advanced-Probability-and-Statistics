import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

subgroups = ['African American', 'Asian', 'Hispanic', 'Native American', 'Pacific Islander', 'White', 'Multiple Races']
num_enrolled = [2769, 636, 26841, 2514, 447, 23035, 2022]
perc_enrolled = np.array([4.75, 1.09, 46.07, 4.32, 0.77, 39.54, 3.47])



studentPop = pd.DataFrame({'Race' : subgroups,
                           'Population': num_enrolled,
                           'Percentage': perc_enrolled})
print(studentPop)

plt.pie(perc_enrolled, labels= subgroups)
plt.legend()
plt.show()