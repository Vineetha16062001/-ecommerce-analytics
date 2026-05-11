import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Sports', 'Books', 'Beauty']
products = {
    'Electronics': ['Laptop', 'Smartphone', 'Headphones', 'Tablet', 'Smartwatch'],
    'Clothing':    ['T-Shirt', 'Jeans', 'Jacket', 'Dress', 'Sneakers'],
    'Home & Kitchen': ['Blender', 'Coffee Maker', 'Air Fryer', 'Cookware Set', 'Vacuum'],
    'Sports':      ['Yoga Mat', 'Dumbbells', 'Running Shoes', 'Cycling Helmet', 'Protein Powder'],
    'Books':       ['Data Science', 'Python Programming', 'Business Analytics', 'AI Fundamentals', 'SQL Mastery'],
    'Beauty':      ['Moisturizer', 'Lipstick', 'Serum', 'Foundation', 'Perfume'],
}
prices = {
    'Electronics': (200, 1500), 'Clothing': (20, 150),
    'Home & Kitchen': (30, 300), 'Sports': (15, 200),
    'Books': (10, 60), 'Beauty': (10, 120),
}
regions   = ['North', 'South', 'East', 'West', 'Central']
channels  = ['Online', 'In-Store', 'Mobile App']
customers = [f'CUST{str(i).zfill(4)}' for i in range(1, 501)]

start = datetime(2023, 1, 1)
rows  = []
for i in range(2000):
    cat     = random.choice(categories)
    product = random.choice(products[cat])
    lo, hi  = prices[cat]
    price   = round(random.uniform(lo, hi), 2)
    qty     = random.randint(1, 10)
    disc    = random.choice([0, 0, 0, 5, 10, 15, 20])
    revenue = round(price * qty * (1 - disc / 100), 2)
    date    = start + timedelta(days=random.randint(0, 364))
    rows.append({
        'order_id':    f'ORD{str(i+1).zfill(5)}',
        'date':        date.strftime('%Y-%m-%d'),
        'customer_id': random.choice(customers),
        'category':    cat,
        'product':     product,
        'region':      random.choice(regions),
        'channel':     random.choice(channels),
        'quantity':    qty,
        'unit_price':  price,
        'discount_pct':disc,
        'revenue':     revenue,
    })

df = pd.DataFrame(rows).sort_values('date').reset_index(drop=True)
df.to_csv('data/sales_data.csv', index=False)
print(f"Generated {len(df)} records -> data/sales_data.csv")
