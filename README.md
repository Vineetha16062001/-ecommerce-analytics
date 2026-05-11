# E-Commerce Sales Analytics Dashboard 📊

A Python-based data analysis project that explores e-commerce sales data to uncover revenue trends, top-performing products, regional performance, and the impact of discounts — using Pandas, Matplotlib, and Seaborn.

---

## Features

- **Monthly Revenue Trend Analysis** — Line chart tracking revenue across all 12 months with annotations
- **Category Performance** — Bar and pie charts breaking down revenue and units sold by product category
- **Region × Channel Heatmap** — Pivot-table heatmap showing revenue across regions and sales channels
- **Top 10 Products** — Horizontal bar chart of best-performing products by total revenue
- **Quarterly Channel Comparison** — Grouped bar chart comparing Online, In-Store, and Mobile App sales
- **Discount Impact Analysis** — Dual-axis chart of discount percentage vs order count and average revenue
- **Summary Report Export** — Auto-generated CSV report with key business metrics
- **Synthetic Dataset Generator** — Reproducible 2,000-row sales dataset with realistic distributions

---

## Architecture

```
+-----------------------------+
|        CLI / Script         |
+-------------+---------------+
              |
+-------------v---------------+
|       analysis.py           |
|   (Main Analysis Engine)    |
+-------------+---------------+
              |
+-------------v---------------+
|      generate_data.py       |
|   (Dataset Generator)       |
+-------------+---------------+
              |
    +---------+---------+
    |                   |
+---v---+         +-----v-----+
| data/ |         |  output/  |
| .csv  |         |  charts   |
+-------+         +-----------+
```

---

## Tech Stack

| Component | Technology |
|---|---|
| Language | Python 3.x |
| Data Manipulation | Pandas |
| Visualization | Matplotlib |
| Statistical Charts | Seaborn |
| Data Format | CSV |

---

## Setup

### Prerequisites

- Python 3.8 or higher
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/Vineetha16062001/ecommerce-sales-analytics.git
cd ecommerce-sales-analytics

# Install dependencies
pip install -r requirements.txt
```

### Running the Project

```bash
# Step 1 — Generate the dataset
python generate_data.py
```

Output:
```
Generated 2000 records -> data/sales_data.csv
```

```bash
# Step 2 — Run the full analysis
python analysis.py
```

Output:
```
=======================================================
   E-COMMERCE SALES ANALYTICS — 2023
=======================================================
  Total Orders    : 2,000
  Total Revenue   : $2,181,732.56
  Avg Order Value : $1,090.87
  Total Units     : 11,120
  Unique Customers: 490
=======================================================
✓ Chart 1: Monthly Revenue Trend
✓ Chart 2: Category Analysis
✓ Chart 3: Region × Channel Heatmap
✓ Chart 4: Top 10 Products
✓ Chart 5: Quarterly Revenue by Channel
✓ Chart 6: Discount Impact Analysis
✓ Summary report saved -> output/summary_report.csv
=======================================================
   ALL CHARTS SAVED TO /output/
=======================================================
```

---

## Key Metrics

| Metric | Value |
|---|---|
| Total Orders | 2,000 |
| Total Revenue | $2,181,732 |
| Avg Order Value | $1,090 |
| Total Units Sold | 11,120 |
| Unique Customers | 490 |
| Categories Analyzed | 6 |
| Regions Covered | 5 |
| Sales Channels | 3 |

---

## Charts Generated

| Chart | File | Description |
|---|---|---|
| Monthly Revenue Trend | `01_monthly_revenue.png` | Revenue across all 12 months |
| Category Analysis | `02_category_analysis.png` | Revenue and units by category |
| Region × Channel Heatmap | `03_region_channel_heatmap.png` | Revenue by region and channel |
| Top 10 Products | `04_top10_products.png` | Best-selling products by revenue |
| Quarterly by Channel | `05_quarterly_channel.png` | Online vs In-Store vs Mobile |
| Discount Impact | `06_discount_impact.png` | Discount % vs revenue and orders |

---

## Project Structure

```
ecommerce-sales-analytics/
├── data/
│   └── sales_data.csv              # Generated dataset (2,000 orders)
├── output/
│   ├── 01_monthly_revenue.png
│   ├── 02_category_analysis.png
│   ├── 03_region_channel_heatmap.png
│   ├── 04_top10_products.png
│   ├── 05_quarterly_channel.png
│   ├── 06_discount_impact.png
│   └── summary_report.csv
├── analysis.py                     # Main analysis and chart generation
├── generate_data.py                # Synthetic dataset generator
├── requirements.txt
└── README.md
```

---

## Future Improvements

- [ ] Interactive dashboard using Streamlit
- [ ] Customer segmentation using RFM analysis
- [ ] Sales forecasting with Linear Regression
- [ ] Real dataset integration (Kaggle / retail APIs)
- [ ] Auto-export full report to PDF
- [ ] Unit tests with pytest
- [ ] REST API with FastAPI for live data

---

## Skills Demonstrated

- Data wrangling with Pandas (groupby, pivot tables, aggregations)
- Time-series analysis (monthly and quarterly trends)
- Multi-chart dashboard layout with Matplotlib
- Statistical and heatmap visualization with Seaborn
- Business insight extraction from raw transactional data
- Reproducible dataset generation with controlled randomness

---

## License

This project is licensed under the MIT License — see the LICENSE file for details.

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'feat: add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## About

E-Commerce Sales Analytics Dashboard built with Python, Pandas, Matplotlib, and Seaborn.

**Languages:** Python 100%
