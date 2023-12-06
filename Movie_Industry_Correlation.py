# Project Overview:
# The goal is to analyze factors affecting a movie's gross revenue in the American movie industry using Python for data analysis.
# more a guidline of code on how to do it, as this gave me trouble. Project would be easier with visualiser like tableau
# We'll use a dataset spanning four decades obtained Data Source: https://www.kaggle.com/danielgrijalvas/movies

# Section 1: Collect and Transform Data
import pandas as pd

# Assuming you have a CSV file named "movies.csv"
df = pd.read_csv("movies.csv")

# Explore the dataset
print(df.head())
print(df.isnull().sum())

# Clean and restructure the data as needed

# Section 2: Find Correlation
# Identify numerical features that might influence gross revenue
# Compute correlation coefficients
correlation_matrix = df.corr()

# Section 3: Visualize Correlations
import seaborn as sns
import matplotlib.pyplot as plt

# Visualize the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

# Create scatter plots or other visualizations for highly correlated pairs
sns.pairplot(df[['feature1', 'feature2', 'gross_revenue']])
plt.show()

# Section 4: Correlate Entire Database and Make Conclusions
# Examine the correlation coefficients and identify patterns
revenue_correlation = correlation_matrix['gross_revenue'].sort_values(ascending=False)
print(revenue_correlation)

# Draw conclusions based on the correlation values and visualizations


# Section 5: Further Analysis (Optional)
# Conduct regression analysis or other statistical techniques for a deeper understanding
