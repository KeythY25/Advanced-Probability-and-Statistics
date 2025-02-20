import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# Data for student scores before and after the intervention
scores_before = np.array([80, 85, 88, 90, 92, 76, 81, 84, 88, 75])
scores_after = np.array([85, 88, 92, 94, 96, 78, 86, 88, 90, 80])

# Calculate average scores before and after
average_before = np.mean(scores_before)
average_after = np.mean(scores_after)

# Assumption Check: Normality (Shapiro-Wilk Test)
_, p_before = stats.shapiro(scores_before)
_, p_after = stats.shapiro(scores_after)

alpha = 0.05  # Significance level

# Create a pair plot to visualize the data before and after the intervention
plt.figure(figsize=(8, 4))
plt.subplot(1, 2, 1)
plt.hist(scores_before, color='b', alpha=0.7, label='Before Intervention')
plt.axvline(average_before, color='b', linestyle='--', label='Average Before')
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.legend()

plt.subplot(1, 2, 2)
plt.hist(scores_after, color='g', alpha=0.7, label='After Intervention')
plt.axvline(average_after, color='g', linestyle='--', label='Average After')
plt.xlabel("Scores")
plt.ylabel("Frequency")
plt.legend()

plt.suptitle("Distribution of Scores Before and After Intervention")
plt.show()

# Perform the t-test if the normality assumption is met
if p_before > alpha and p_after > alpha:
    t_stat, p_value = stats.ttest_rel(scores_before, scores_after)
    print("Paired Data T-Test Results (Normality Assumption Met):")
    print("t-statistic:", t_stat)
    print("p-value:", p_value)
    
    # Create a box plot to visualize the before and after scores
    plt.figure()
    plt.boxplot([scores_before, scores_after], labels=['Before Intervention', 'After Intervention'])
    plt.ylabel("Scores")
    plt.title("Box Plot of Scores Before and After Intervention")
    plt.show()

else:
    # If normality assumption is violated, perform Wilcoxon Signed Rank Test
    w_stat, p_value = stats.wilcoxon(scores_before, scores_after)
    print("Wilcoxon Signed Rank Test Results (Normality Assumption Violated):")
    print("W-statistic:", w_stat)
    print("p-value:", p_value)

    # Create a paired data scatter plot
    plt.figure()
    plt.scatter(scores_before, scores_after)
    plt.xlabel("Scores Before Intervention")
    plt.ylabel("Scores After Intervention")
    plt.title("Paired Data Scatter Plot")
    plt.show()

# Print average scores
print("Average Score Before Intervention:", average_before)
print("Average Score After Intervention:", average_after)
