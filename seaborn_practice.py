import seaborn as sns
import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
print(tips.head())

plt.figure(figsize=(10, 5))
sns.scatterplot(data=tips, x='day',y='total_bill',hue='smoker')
plt.title("total bill vs tip")
plt.xlabel("total bill ($)")
plt.ylabel("tip ($)")

plt.show()