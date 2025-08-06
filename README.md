# ETL Data Pipeline Project

This project demonstrates a basic ETL (Extract, Transform, Load) pipeline using Python, Pandas, and SQLite. It simulates a stock trading scenario by processing raw trade data, performing transformations, filtering high-value trades, and storing the results for querying.

## Features

- Load raw trade data from CSV
- Calculate total trade value (`price × volume`)
- Filter trades with value > 50,000
- Save the cleaned data to a new CSV file
- Store filtered data in a SQLite database
- Run SQL queries to extract insights

## Tech Stack

- Python 3.13
- Pandas
- SQLite
- VS Code

## Files

- `stock_data.csv` – Sample trade data
- `read_stock_data.py` – Extracts and transforms data
- `high_value_trades.csv` – Output after filtering
- `load_to_sqlite.py` – Loads data into SQLite
- `query_db.py` – Queries database for results

## How to Run

```bash
python read_stock_data.py
python load_to_sqlite.py
python query_db.py
Use Case
Built for showcasing beginner-level data engineering skills aligned with StoneX apprenticeship expectations.

yaml
Copy
Edit

---

You can now:
1. Save this as `README.md`
2. Run `git add README.md && git commit -m "Add README"`  
3. Then push: `git push origin main`
