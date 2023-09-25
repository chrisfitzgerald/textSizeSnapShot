import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# Load your CSV file into a DataFrame
df = pd.read_csv('documents_dataset.csv')

# Assuming 'text_size' is the column of interest from your dataset
bins = [0, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, float('inf')]
labels = ['0-100', '101-500', '501-1k', '1k-5k', '5k-10k', '10k-50k', '50k-100k', '100k-500k', '500k-1M', '1M+']
df['size_range'] = pd.cut(df['text_size'], bins=bins, labels=labels)

# Data preparation
doc_count_per_bin = df['size_range'].value_counts().reindex(labels)
text_size_sum_per_bin = df.groupby('size_range')['text_size'].sum()
heatmap_data = pd.DataFrame({
    'Number of Documents': doc_count_per_bin,
    'Total Text Size': text_size_sum_per_bin
}).T
data_text_size = pd.DataFrame({'Total Text Size': heatmap_data.loc['Total Text Size']}).T
data_doc_count = pd.DataFrame({'Number of Documents': heatmap_data.loc['Number of Documents']}).T

# Setting color scale limits
vmin = heatmap_data.min().min()
vmax_text_size = heatmap_data.loc['Total Text Size'].max() / 10  # Aggressive limit for Total Text Size
vmax_doc_count = heatmap_data.loc['Number of Documents'].max() / 3  # Separate limit for Number of Documents

# Plotting the heatmaps in separate subplots
fig, axs = plt.subplots(2, 1, figsize=(14, 10))

# Heatmap for Total Text Size
sns.heatmap(data_text_size, cmap="YlGnBu", annot=True, fmt=".0f", cbar_kws={'label': 'Magnitude for Text Size'}, vmin=vmin, vmax=vmax_text_size, ax=axs[0])
axs[0].set_title("Total Text Size by Binned Range")

# Heatmap for Number of Documents
sns.heatmap(data_doc_count, cmap="OrRd", annot=True, fmt=".0f", cbar_kws={'label': 'Magnitude for Document Count'}, vmin=vmin, vmax=vmax_doc_count, ax=axs[1])
axs[1].set_title("Number of Documents by Binned Range")

plt.tight_layout()
plt.show()