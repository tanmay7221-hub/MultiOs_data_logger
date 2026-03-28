import pandas as pd
import sqlite3
import matplotlib.pyplot as plt

# ---- Load CSV ----
csv_file = "data/sample.csv"
df = pd.read_csv(csv_file)
print("CSV Loaded:\n", df)

# ---- Load Binary ----
bin_file = "data/sample.bin"
with open(bin_file, "rb") as f:
    binary_data = f.read().decode("utf-8", errors="ignore")
print("\nBinary Data:\n", binary_data)

# ---- Insert into SQLite DB ----
conn = sqlite3.connect("data/data.db")
df.to_sql("sales_table", conn, if_exists="replace", index=False)
print("\nData inserted into SQLite database")

# ---- Query & Visualize ----
df_db = pd.read_sql("SELECT * FROM sales_table", conn)
df_db.plot(x="name", y="sales", kind="bar", title="Sales Data")
plt.show()

conn.close()
