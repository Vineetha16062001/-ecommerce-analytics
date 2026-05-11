"""
E-Commerce Sales Analytics Dashboard
=====================================
Author : Vineetha Rangineni
Tools  : Python, Pandas, Matplotlib, Seaborn
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import seaborn as sns
import os

# ── Setup ──────────────────────────────────────────────────────────────────────
os.makedirs('output', exist_ok=True)

sns.set_theme(style='whitegrid', palette='muted')
COLORS = ['#2196F3', '#4CAF50', '#FF9800', '#E91E63', '#9C27B0', '#00BCD4']

# ── Load Data ──────────────────────────────────────────────────────────────────
df = pd.read_csv('data/sales_data.csv', parse_dates=['date'])
df['month']   = df['date'].dt.to_period('M').astype(str)
df['month_n'] = df['date'].dt.month
df['quarter'] = 'Q' + df['date'].dt.quarter.astype(str)

print("=" * 55)
print("   E-COMMERCE SALES ANALYTICS — 2023")
print("=" * 55)
print(f"  Total Orders   : {len(df):,}")
print(f"  Total Revenue  : ${df['revenue'].sum():,.2f}")
print(f"  Avg Order Value: ${df['revenue'].mean():,.2f}")
print(f"  Total Units    : {df['quantity'].sum():,}")
print(f"  Unique Customers: {df['customer_id'].nunique():,}")
print("=" * 55)

# ══════════════════════════════════════════════════════════════════════════════
# CHART 1 — Monthly Revenue Trend
# ══════════════════════════════════════════════════════════════════════════════
monthly = df.groupby('month')['revenue'].sum().reset_index()

fig, ax = plt.subplots(figsize=(12, 5))
ax.fill_between(monthly['month'], monthly['revenue'], alpha=0.15, color=COLORS[0])
ax.plot(monthly['month'], monthly['revenue'], color=COLORS[0], linewidth=2.5, marker='o', markersize=6)
for i, row in monthly.iterrows():
    ax.annotate(f"${row['revenue']/1000:.1f}K", (row['month'], row['revenue']),
                textcoords='offset points', xytext=(0, 8), ha='center', fontsize=8)
ax.set_title('Monthly Revenue Trend — 2023', fontsize=14, fontweight='bold', pad=15)
ax.set_xlabel('Month')
ax.set_ylabel('Revenue ($)')
ax.tick_params(axis='x', rotation=45)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x/1000:.0f}K'))
plt.tight_layout()
plt.savefig('output/01_monthly_revenue.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Chart 1: Monthly Revenue Trend")

# ══════════════════════════════════════════════════════════════════════════════
# CHART 2 — Revenue by Category (Bar + Pie side by side)
# ══════════════════════════════════════════════════════════════════════════════
cat_rev  = df.groupby('category')['revenue'].sum().sort_values(ascending=False)
cat_qty  = df.groupby('category')['quantity'].sum().sort_values(ascending=False)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

bars = ax1.bar(cat_rev.index, cat_rev.values, color=COLORS, edgecolor='white', linewidth=0.5)
for bar, val in zip(bars, cat_rev.values):
    ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 500,
             f'${val/1000:.1f}K', ha='center', va='bottom', fontsize=9, fontweight='bold')
ax1.set_title('Revenue by Category', fontsize=13, fontweight='bold')
ax1.set_ylabel('Revenue ($)')
ax1.tick_params(axis='x', rotation=20)
ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x/1000:.0f}K'))

wedges, texts, autotexts = ax2.pie(
    cat_qty.values, labels=cat_qty.index, autopct='%1.1f%%',
    colors=COLORS, startangle=140, pctdistance=0.82,
    wedgeprops=dict(edgecolor='white', linewidth=1.5))
for at in autotexts:
    at.set_fontsize(9)
ax2.set_title('Units Sold by Category', fontsize=13, fontweight='bold')

plt.tight_layout()
plt.savefig('output/02_category_analysis.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Chart 2: Category Analysis")

# ══════════════════════════════════════════════════════════════════════════════
# CHART 3 — Sales Channel & Region Heatmap
# ══════════════════════════════════════════════════════════════════════════════
pivot = df.pivot_table(values='revenue', index='region', columns='channel', aggfunc='sum')

fig, ax = plt.subplots(figsize=(10, 5))
sns.heatmap(pivot, annot=True, fmt=',.0f', cmap='Blues',
            linewidths=0.5, linecolor='white', ax=ax,
            annot_kws={'size': 10})
ax.set_title('Revenue Heatmap: Region × Sales Channel', fontsize=13, fontweight='bold', pad=15)
ax.set_xlabel('Sales Channel')
ax.set_ylabel('Region')
plt.tight_layout()
plt.savefig('output/03_region_channel_heatmap.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Chart 3: Region × Channel Heatmap")

# ══════════════════════════════════════════════════════════════════════════════
# CHART 4 — Top 10 Products by Revenue
# ══════════════════════════════════════════════════════════════════════════════
top10 = df.groupby('product')['revenue'].sum().sort_values(ascending=True).tail(10)

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(top10.index, top10.values,
               color=sns.color_palette('Blues_r', len(top10)), edgecolor='white')
for bar, val in zip(bars, top10.values):
    ax.text(val + 200, bar.get_y() + bar.get_height()/2,
            f'${val/1000:.1f}K', va='center', fontsize=9, fontweight='bold')
ax.set_title('Top 10 Products by Revenue', fontsize=13, fontweight='bold', pad=15)
ax.set_xlabel('Revenue ($)')
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x/1000:.0f}K'))
ax.spines[['top', 'right']].set_visible(False)
plt.tight_layout()
plt.savefig('output/04_top10_products.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Chart 4: Top 10 Products")

# ══════════════════════════════════════════════════════════════════════════════
# CHART 5 — Quarterly Revenue by Channel
# ══════════════════════════════════════════════════════════════════════════════
qtr_ch = df.groupby(['quarter', 'channel'])['revenue'].sum().reset_index()
qtr_pivot = qtr_ch.pivot(index='quarter', columns='channel', values='revenue')

fig, ax = plt.subplots(figsize=(10, 6))
qtr_pivot.plot(kind='bar', ax=ax, color=COLORS[:3], edgecolor='white', width=0.7)
ax.set_title('Quarterly Revenue by Sales Channel', fontsize=13, fontweight='bold', pad=15)
ax.set_xlabel('Quarter')
ax.set_ylabel('Revenue ($)')
ax.tick_params(axis='x', rotation=0)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x/1000:.0f}K'))
ax.legend(title='Channel', bbox_to_anchor=(1.01, 1), loc='upper left')
ax.spines[['top', 'right']].set_visible(False)
plt.tight_layout()
plt.savefig('output/05_quarterly_channel.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Chart 5: Quarterly Revenue by Channel")

# ══════════════════════════════════════════════════════════════════════════════
# CHART 6 — Discount Impact on Revenue
# ══════════════════════════════════════════════════════════════════════════════
disc_rev = df.groupby('discount_pct').agg(
    avg_revenue=('revenue', 'mean'),
    order_count=('order_id', 'count')
).reset_index()

fig, ax1 = plt.subplots(figsize=(10, 5))
ax2 = ax1.twinx()
ax1.bar(disc_rev['discount_pct'].astype(str) + '%', disc_rev['order_count'],
        color=COLORS[1], alpha=0.6, label='Order Count')
ax2.plot(disc_rev['discount_pct'].astype(str) + '%', disc_rev['avg_revenue'],
         color=COLORS[3], linewidth=2.5, marker='D', markersize=8, label='Avg Revenue')
ax1.set_title('Discount % vs Order Count & Avg Revenue', fontsize=13, fontweight='bold', pad=15)
ax1.set_xlabel('Discount %')
ax1.set_ylabel('Order Count', color=COLORS[1])
ax2.set_ylabel('Avg Revenue ($)', color=COLORS[3])
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper right')
plt.tight_layout()
plt.savefig('output/06_discount_impact.png', dpi=150, bbox_inches='tight')
plt.close()
print("✓ Chart 6: Discount Impact Analysis")

# ══════════════════════════════════════════════════════════════════════════════
# SUMMARY REPORT — CSV
# ══════════════════════════════════════════════════════════════════════════════
summary = pd.DataFrame({
    'Metric': [
        'Total Orders', 'Total Revenue', 'Avg Order Value',
        'Total Units Sold', 'Unique Customers',
        'Best Category', 'Best Region', 'Best Channel',
        'Highest Revenue Month',
    ],
    'Value': [
        f"{len(df):,}",
        f"${df['revenue'].sum():,.2f}",
        f"${df['revenue'].mean():,.2f}",
        f"{df['quantity'].sum():,}",
        f"{df['customer_id'].nunique():,}",
        df.groupby('category')['revenue'].sum().idxmax(),
        df.groupby('region')['revenue'].sum().idxmax(),
        df.groupby('channel')['revenue'].sum().idxmax(),
        monthly.loc[monthly['revenue'].idxmax(), 'month'],
    ]
})
summary.to_csv('output/summary_report.csv', index=False)
print("✓ Summary report saved -> output/summary_report.csv")

print("\n" + "=" * 55)
print("   ALL CHARTS SAVED TO /output/")
print("=" * 55)
