
from pathlib import Path
import pandas as pd
import re

base = Path.home() / "OneDrive" / "Desktop" / "Kenya County Budget Intelligence"

cleaned = base / "Data" / "Cleaned"
processed = base / "Data" / "Processed"
processed.mkdir(parents=True, exist_ok=True)

datasets = {
    "development.csv": "development_long.csv",
    "own_source_revenue.csv": "own_source_revenue_long.csv",
    "pending_bills.csv": "pending_bills_long.csv"
}

for source_file, output_file in datasets.items():

    df = pd.read_csv(cleaned / source_file)

    # Keep only genuine financial-year columns
    year_columns = [
        col for col in df.columns
        if re.fullmatch(r"\d{4}/\d{2}", str(col).strip())
    ]

    if not year_columns:
        raise ValueError(f"No financial-year columns found in {source_file}")

    long_df = df.melt(
        id_vars=["Code", "County"],
        value_vars=year_columns,
        var_name="Financial_Year",
        value_name="Amount"
    )

    long_df["Amount"] = pd.to_numeric(
        long_df["Amount"], errors="coerce"
    )

    long_df.to_csv(processed / output_file, index=False)

    print(f"\nCreated: {output_file}")
    print(f"Records: {len(long_df)}")
    print(f"Financial years: {len(year_columns)}")

print("\nALL DATASETS RESHAPED SUCCESSFULLY")
