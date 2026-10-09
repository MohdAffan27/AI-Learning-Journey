# 📊 Seaborn - Statistical Data Visualization

## 📌 Introduction

Seaborn is a Python data visualization library built on top of Matplotlib. It provides a high-level interface for creating attractive and informative statistical graphics.

This repository contains my Seaborn learning notes and examples as part of my **AI/ML Learning Journey**.

## 🎯 Learning Objectives

- Understand the fundamentals of Seaborn.
- Create different types of statistical plots.
- Visualize relationships between variables.
- Analyze data distributions.
- Explore correlations using heatmaps.
- Visualize relationships among multiple variables using pair plots.

## 📚 Topics Covered

### 1. Introduction to Seaborn

- Introduction to Seaborn
- Basic plotting concepts
- Working with datasets

### 2. Basic Plots in Seaborn

- **Line Plot** — Visualizing trends and changes in data.
- **Scatter Plot** — Exploring relationships between two numerical variables.
- **Bar Plot** — Comparing aggregated values across categories.
- **Box Plot** — Understanding data distribution, quartiles, and potential outliers.
- **Histogram** — Visualizing the frequency distribution of numerical data.
- **Heatmap** — Representing values using colors, commonly for correlation matrices.
- **Pair Plot** — Exploring pairwise relationships among multiple numerical variables.

## 💻 Basic Example

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Load a sample dataset
df = sns.load_dataset("tips")

# Create a scatter plot
sns.scatterplot(
    data=df,
    x="total_bill",
    y="tip",
    hue="sex"
)

# Add a title
plt.title("Relationship Between Total Bill and Tip")

# Display the plot
plt.show()
```

## 🛠️ Tools and Technologies

- **Programming Language:** Python
- **Visualization Libraries:** Seaborn and Matplotlib
- **Environment:** Jupyter Notebook
- **Version Control:** Git and GitHub

## 📈 Learning Outcomes

After learning these topics, I gained an understanding of:

- Creating statistical visualizations using Seaborn.
- Comparing numerical and categorical data.
- Understanding distributions and potential outliers.
- Exploring relationships between variables.
- Visualizing correlations through heatmaps.
- Using pair plots for multivariate exploratory analysis.

## 🚀 Next Steps

- Practice Seaborn with real-world datasets.
- Explore additional plot customization options.
- Combine Seaborn with Pandas and Matplotlib.
- Apply visualization techniques to Exploratory Data Analysis (EDA).
- Use these skills in Machine Learning projects.

---

**Part of my AI/ML Learning Journey** — learning, practicing, and building practical skills in Data Science and Machine Learning.
