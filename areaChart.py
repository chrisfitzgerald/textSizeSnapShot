import pandas as pd
import matplotlib.pyplot as plt

# Load your CSV file into a DataFrame
df = pd.read_csv('documents_dataset2.csv')

# Static bin sizes and labels
bins = [0, 100, 500, 1000, 5000, 10000, 50000, 100000, 500000, 1000000, float('inf')]
labels = ['0-100', '101-500', '501-1k', '1k-5k', '5k-10k', '10k-50k', '50k-100k', '100k-500k', '500k-1M', '1M+']
df['size_range'] = pd.cut(df['text_size'], bins=bins, labels=labels)

# Data preparation
doc_count_per_bin = df['size_range'].value_counts().reindex(labels)
text_size_sum_per_bin = df.groupby('size_range')['text_size'].sum()

fig, ax1 = plt.subplots(figsize=(14, 7))

# Bar chart for Total Text Size
ax1.bar(text_size_sum_per_bin.index, text_size_sum_per_bin, color='lightblue', label='Total Text Size', alpha=0.8)
ax1.set_xlabel('Text Size Range')
ax1.set_ylabel('Total Text Size', color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
ax1.set_title("Comparison of Total Text Size and Number of Documents by Binned Range")
ax1.set_xticks(range(len(text_size_sum_per_bin.index)))
ax1.set_xticklabels(text_size_sum_per_bin.index, rotation=45)

# Area chart and Line chart for Number of Documents
ax2 = ax1.twinx()
ax2.fill_between(doc_count_per_bin.index, 0, doc_count_per_bin, color='lightcoral', alpha=0.5, label='Number of Documents (Area)')
ax2.plot(doc_count_per_bin.index, doc_count_per_bin, color='darkred', label='Number of Documents (Line)', linewidth=2)
ax2.set_ylabel('Number of Documents', color='darkred')
ax2.tick_params(axis='y', labelcolor='darkred')

# Align the zero points of both axes
ax1_ylim = ax1.get_ylim()
ax2_ylim = ax2.get_ylim()
aligned_zero = max(ax1_ylim[0]/ax1_ylim[1], ax2_ylim[0]/ax2_ylim[1])
ax1.set_ylim([aligned_zero * ax1_ylim[1], ax1_ylim[1]])
ax2.set_ylim([aligned_zero * ax2_ylim[1], ax2_ylim[1]])

plt.tight_layout()
plt.show()
