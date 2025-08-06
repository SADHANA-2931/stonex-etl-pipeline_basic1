# 📊 StoneX ETL Data Pipeline Project (Beginner Friendly)

This is a beginner-friendly **ETL (Extract, Transform, Load)** pipeline project built using **Python**, **Pandas**, and **SQLite**.  
It simulates a real-world **financial data pipeline** you might encounter in an apprenticeship at **StoneX** or other global fintech companies.

---

## 🚀 Project Overview

This mini-project mimics how stock market trade data is:
- 📥 Extracted from a CSV file
- 🔧 Transformed by applying business rules
- 🗃️ Loaded into a database for querying

It includes:
- Reading raw stock trade data
- Adding a new column `trade_value = price * volume`
- Filtering only high-value trades (above ₹50,000)
- Storing cleaned data in both CSV and SQLite database
- Querying specific results using SQL

---

## 📁 Project Structure

```bash
stonex_etl_project/
│
├── stock_data.csv            # Sample input data
├── high_value_trades.csv     # Output after filtering
│
├── read_stock_data.py        # Extract + Transform + Filter + Save
├── load_to_sqlite.py         # Load cleaned data into SQLite DB
├── query_db.py               # SQL query to fetch specific records
├── hello.py                  # Initial test script
└── README.md                 # This file
