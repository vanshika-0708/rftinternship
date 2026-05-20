import matplotlib.pyplot as plt

# Dataset
DATES = ["MON", "TUE", "WED", "THU", "FRI"]
SALES = [200, 250, 300, 280, 350]

# Find highest and lowest
max_idx = SALES.index(max(SALES))
min_idx = SALES.index(min(SALES))

# Plot
fig, ax = plt.subplots(figsize=(8, 5))

ax.plot(DATES, SALES, marker='o', color='steelblue', linewidth=2.5, label='Daily Sales')

# Highlight highest day (green)
ax.scatter(DATES[max_idx], SALES[max_idx], color='green', s=150, zorder=5, label=f'Highest: {SALES[max_idx]}')
ax.annotate(f'Highest\n{SALES[max_idx]}',
            xy=(DATES[max_idx], SALES[max_idx]),
            xytext=(max_idx - 0.4, SALES[max_idx] + 10),
            fontsize=10, color='green', fontweight='bold')

# Highlight lowest day (red)
ax.scatter(DATES[min_idx], SALES[min_idx], color='red', s=150, zorder=5, label=f'Lowest: {SALES[min_idx]}')
ax.annotate(f'Lowest\n{SALES[min_idx]}',
            xy=(DATES[min_idx], SALES[min_idx]),
            xytext=(min_idx + 0.1, SALES[min_idx] - 20),
            fontsize=10, color='red', fontweight='bold')

# Labels & Title
ax.set_title('Weekly Sales Trend', fontsize=16, fontweight='bold')
ax.set_xlabel('Day of the Week', fontsize=12)
ax.set_ylabel('Sales (Units)', fontsize=12)
ax.legend()
ax.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.savefig('sales_trend.png', dpi=150)
plt.show()