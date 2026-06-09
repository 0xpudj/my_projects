import pandas as pd
import numpy as np
import matplotlib as mpl
import seaborn as sns
import matplotlib.pyplot as plt

## PART 01 : Data Preparation
# Load the sales.csv file or generate data
# df = pd.read_csv("sales.csv")

n = 10
data = {"Customer_ID": np.arange(1 , n+1),
      "Gendre": np.random.choice(["M","F"],size= n),
      "Age": np.random.randint(18,70,size= n),
      "City": np.random.choice(["Algeria","Oran","Annaba","Jijel"],size= n),
      "Purchase_Amount": np.random.randint(50,501,size= n)*10,
      "Number_Orders": np.random.randint(1,11,size= n)}

df = pd.DataFrame(data)

# Display the first few rows
print(df.head(10))

# Display general information
print("\nGeneral information:")
print(df.info(),'\n')

# Display descriptive statistics
print("\nDescriptive statistics:\n",df.describe(),'\n')

## PART 02 : Descriptive Statistics
# Calculate:mean,median,mode,minimum,maximum,variance,standard deviation
print("statistic of Purchase_Amount:")
print(f"The mean is: {df["Purchase_Amount"].mean()}")
print(f"The median is: {df["Purchase_Amount"].median()}")
print(f"The mode is:\n {df["Purchase_Amount"].mode().reset_index()}\n")
print(f"The min is: {df["Purchase_Amount"].min()}")
print(f"The max is: {df["Purchase_Amount"].max()}")
print(f"The variance is: {df["Purchase_Amount"].var()}")
print(f"The standard deviation is: {df["Purchase_Amount"].std()}")

# Determine average age by gender
avg_age_by_gender = df.groupby("Gendre")["Age"].mean().astype(int)
print(f"\nAverage age by gender:\n{avg_age_by_gender.reset_index()}")

# The city with the highest spending
the_city_highest_spending = df.groupby("City")["Purchase_Amount"].sum().idxmax()
print(f"\nThe city with the highest spending: {the_city_highest_spending}")

# Count number of customers by gender
## customer_count_by_gender = df["Gendre"].value_counts()
customer_count_by_gender = df.groupby("Gendre")["Customer_ID"].count()
print(f"\nNumber of customers by gender:\n {customer_count_by_gender.reset_index()}")

## PART 03 : Visualization
# Histogram of age distribution
sns.histplot(data=df, x="Age", hue="Gendre", kde=True, bins=10)

plt.title("Age Distribution of Customers")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()

# Boxplot of Purchase_Amount by Gender
sns.boxplot(data=df, x="Gendre", y="Purchase_Amount", palette="pastel")

plt.title("Purchase Amount by Gender")
plt.xlabel("Gender")
plt.ylabel("Purchase Amount")
plt.show()

# Bar chart of number of customers by city
customers_by_city = df.groupby("City")["Customer_ID"].count().reset_index()
customers_by_city.columns = ["City", "Customer_Count"]
sns.barplot(data=customers_by_city, x="City", y="Customer_Count", palette="muted")

plt.title("Number of Customers by City")
plt.xlabel("City")
plt.ylabel("Number of Customers")
plt.show()

# Scatter plot of Age vs Purchase_Amount
sns.scatterplot(data=df, x="Age", y="Purchase_Amount", hue="Gendre", palette="muted")
plt.title("Age vs Purchase Amount")
plt.xlabel("Age")
plt.ylabel("Purchase Amount")
plt.show()

## PART 04 : Interpretation
# Analyze the obtained results: general trends, differences according to gender or city, and relationship between age and purchase amount
print("\n=== Interpretation of Results ===")
print("1️⃣ Age Distribution:")
print("   • The histogram shows how customer ages are distributed. Most customers might belong to a specific age group, indicating a key market segment.\n")

print("2️⃣ Purchase Amount by Gender:")
print("   • The boxplot shows differences in spending between male and female customers. A higher median or wider spread indicates greater spending variation.\n")

print("3️⃣ Customers by City:")
print("   • The bar chart displays which cities have the highest number of customers. Cities with fewer customers may represent growth opportunities.\n")

print("4️⃣ Age vs Purchase Amount:")
print("   • The scatter plot highlights the relationship between age and purchase amount. A positive trend means older customers spend more, while no trend suggests spending is consistent across ages.\n")

print("✅ Overall Insight:")
print("   • These analyses help identify which demographics and regions drive the most sales, guiding better marketing and business decisions.")
