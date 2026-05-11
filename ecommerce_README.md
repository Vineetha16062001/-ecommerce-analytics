# E-Commerce Sales Analytics Dashboard 📊

A Python-based data analysis project that explores e-commerce sales data to uncover revenue trends, top-performing products, regional insights, and the impact of discounts — using Pandas, Matplotlib, and Seaborn.

---

## 📈 Key Insights Generated

| Metric | Value |
|---|---|
| Total Orders | 2,000 |
| Total Revenue | $2,181,732 |
| Avg Order Value | $1,090 |
| Total Units Sold | 11,120 |
| Unique Customers | 490 |

---

## 📊 Charts & Analysis

| Chart | Description |
|---|---|
| Monthly Revenue Trend | Line chart showing revenue across all 12 months |
| Category Analysis | Bar + Pie charts for revenue and units by category |
| Region × Channel Heatmap | Revenue breakdown by region and sales channel |
| Top 10 Products | Horizontal bar chart of best-selling products |
| Quarterly Revenue by Channel | Grouped bar chart comparing Online, In-Store, Mobile |
| Discount Impact | Dual-axis chart of discount % vs order count & revenue |

---

## 🗂️ Project Structure

```
ecommerce-analytics/
├── data/
│   └── sales_data.csv        # Generated dataset (2000 orders)
├── output/
│   ├── 01_monthly_revenue.png
│   ├── 02_category_analysis.png
│   ├── 03_region_channel_heatmap.png
│   ├── 04_top10_products.png
│   ├── 05_quarterly_channel.png
│   ├── 06_discount_impact.png
│   └── summary_report.csv
├── generate_data.py          # Generates synthetic sales dataset
├── analysis.py               # Main analysis & chart generation
├── requirements.txt
└── README.md
```

---

## 🧰 Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.x | Core language |
| Pandas | Data manipulation & aggregation |
| Matplotlib | Chart generation |
| Seaborn | Statistical visualizations |

---

## 🚀 Getting Started

**1. Clone the repository**
```bash
git clone https://github.com/Vineetha16062001/ecommerce-analytics.git
cd ecommerce-analytics
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Generate the dataset**
```bash
python generate_data.py
```

**4. Run the analysis**
```bash
python analysis.py
```

All charts will be saved to the `output/` folder.

---

## 💡 Skills Demonstrated

- Data wrangling with Pandas (groupby, pivot tables, aggregations)
- Time-series analysis (monthly & quarterly trends)
- Multi-chart dashboard layout with Matplotlib
- Heatmap and statistical visualization with Seaborn
- Business insight extraction from raw data

---

## 🔮 Planned Enhancements

- [ ] Interactive dashboard using Streamlit
- [ ] Customer segmentation (RFM analysis)
- [ ] Sales forecasting with Linear Regression
- [ ] Export report to PDF automatically

---

## 📄 License

MIT License — free to use and modify.

---

## 🙋 Author

**Vineetha Rangineni** — [@Vineetha16062001](https://github.com/Vineetha16062001)  
MS-IST @ University of North Texas | Python | SQL | Data Analytics
