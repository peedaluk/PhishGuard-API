from sqlalchemy import text
import pandas as pd
import models       # Import your table definitions
import database     # Import your connection logic


database.Base.metadata.create_all(bind=database.engine)

# 2. Connect and Query
# We reuse the engine from database.py to ensure we look at the SAME file
try:
    with database.engine.connect() as conn:
        # Check if table has data
        result = pd.read_sql(text("SELECT * FROM scan_results ORDER BY id DESC"), conn)

    # 3. Display
    if result.empty:
        print("\n[!] Database exists, but the 'scan_results' table is empty.")
        print("    -> Run the API and scan a URL to generate data!")
    else:
        print("\n[+] --- Database Scan Log ---")
        print(result.to_string(index=False))
        print(f"\n[+] Total Scans: {len(result)}")

except Exception as e:
    print(f"[-] Error querying database: {e}")