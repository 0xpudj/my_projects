import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from scipy.stats import levene , ttest_ind , ttest_1samp
import seaborn as sns
#Generate and save the customer_feedback.csv file
n = 50
data = {
        "satisfaction level": np.clip(np.random.normal(7, 2, n), 0, 10).round(3),
        "gendre": np.random.choice(["M","F"], size=n),
        "waiting time": np.clip(np.random.normal(15, 5, n), 0, None).round(3),
        }

df = pd.DataFrame(data)
#df.to_csv("customer_feedback.csv", index=False)

# Inspect the data (first rows, dimensions, types)
print(df.head())
print("\nDataframe dimensions:", df.shape)
print("\nDataframe info:")
print(df.info())

# Calculate descriptive statistics
print("\nDescriptive statistics:\n", df.describe())

# Part 02:
# point estimation
mean_sat = df["satisfaction level"].mean()
print(f"\nPoint estimation (mean satisfaction level): {mean_sat:.3f}")

# confidence interval 
std_sat = df['satisfaction level'].std(ddof=1)
se = std_sat / np.sqrt(n)
confidence_level = 0.95
degrees_freedom = n - 1
confidence_interval = stats.t.interval(confidence_level, degrees_freedom, mean_sat, se)
print(f"\n95% Confidence interval for satisfaction level: {confidence_interval[0]:.3f} to {confidence_interval[1]:.3f}")

# hypothesis testing
# test 1: Satisfaction Level
hypothesized_mean = 7
t_statistic, p_value = stats.ttest_1samp(df["satisfaction level"], hypothesized_mean)

if t_statistic < 0:
        p_one_tailed_1 = p_value / 2
else:
        p_one_tailed_1 = 1 - p_value / 2

# test 2: gender difference in satisfaction level
group_m = df[df["gendre"]=="M"]["satisfaction level"]
group_f = df[df["gendre"]=="F"]["satisfaction level"]
number_m , number_f = len(group_m) , len(group_f)
stat, p_levene = levene(group_m, group_f)
if p_levene < 0.05:
        t_stat, p_value = ttest_ind(group_m, group_f, equal_var=False)
else:
        t_stat, p_value = ttest_ind(group_m, group_f, equal_var=True)
print(f"t-statistic: {t_stat:.3f}, p-value: {p_value:.3f}")

# Test 3: Waiting Time
hypothesized_mean = 8
t_stat, p_value = ttest_1samp(df['waiting time'], popmean=hypothesized_mean)

alpha = 0.05
print(f"t-statistic: {t_stat:.3f}, two-tailed p-value: {p_value:.3f}")
if p_value < alpha:
        print("Reject H0: Average waiting time is significantly different from 8 minutes")
        if df['waiting time'].mean() > 8:
                print("Recommendation: Reduce waiting time by improving service efficiency.")
        else:
                print("Recommendation: Waiting time is below target; maintain or optimize other areas.")
else:
        print("Fail to reject H0: No evidence that average waiting time differs from 8 minutes")
        print("Recommendation: Waiting time meets the standard; continue monitoring.")

sns.set(style="whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# 1️⃣ Satisfaction distribution with thresholds
sns.histplot(df['satisfaction level'], bins=10, kde=True, color='skyblue', ax=axes[0,0])
axes[0,0].axvline(7, color='red', linestyle='--', label='Target: 7')
axes[0,0].set_title('Satisfaction Level Distribution')
axes[0,0].set_xlabel('Satisfaction Level')
axes[0,0].set_ylabel('Frequency')
axes[0,0].legend()

# 2️⃣ Satisfaction boxplot by gender
sns.boxplot(x='gendre', y='satisfaction level', data=df, palette='Pastel1', ax=axes[0,1])
axes[0,1].set_title('Satisfaction Level by Gender')
axes[0,1].set_xlabel('Gender')
axes[0,1].set_ylabel('Satisfaction Level')

# 3️⃣ Waiting time distribution with target
sns.histplot(df['waiting time'], bins=10, kde=True, color='lightgreen', ax=axes[1,0])
axes[1,0].axvline(8, color='red', linestyle='--', label='Target: 8 min')
axes[1,0].set_title('Waiting Time Distribution')
axes[1,0].set_xlabel('Waiting Time (minutes)')
axes[1,0].set_ylabel('Frequency')
axes[1,0].legend()

# 4️⃣ Scatter plot of satisfaction vs waiting time
sns.scatterplot(x='waiting time', y='satisfaction level', hue='gendre', data=df, palette='Set1', s=80, ax=axes[1,1])
axes[1,1].axhline(7, color='gray', linestyle='--', label='Satisfaction Target')
axes[1,1].axvline(8, color='blue', linestyle='--', label='Waiting Time Target')
axes[1,1].set_title('Satisfaction vs Waiting Time')
axes[1,1].set_xlabel('Waiting Time (minutes)')
axes[1,1].set_ylabel('Satisfaction Level')
axes[1,1].legend()

plt.tight_layout()
plt.show()