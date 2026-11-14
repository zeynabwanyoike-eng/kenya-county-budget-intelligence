from pathlib import Path
import pandas as pd

# Project folders
base = Path.home() / "OneDrive" / "Desktop" / "Kenya County Budget Intelligence"
raw = base / "Data" / "Raw"
cleaned = base / "Data" / "Cleaned"

# Source workbooks and worksheet names
datasets = {
    "development": {
        "file": "kenya-county-development-spending--fy-2013-14---2025-26.xlsx",
        "sheet": "County_by_year"
    },
    "own_source_revenue": {
        "file": "kenya-county-own-source-revenue--fy-2013-14---2025-26.xlsx",
        "sheet": "County_OSR_by_year"
    },
    "pending_bills": {
        "file": "kenya-county-pending-bills--fy-2013-14---2025-26.xlsx",
        "sheet": "County_by_year"
    }
}

for name, details in datasets.items():

    file_path = raw / details["file"]

    # Read the actual column headings from Excel row 3
    df = pd.read_excel(
        file_path,
        sheet_name=details["sheet"],
        header=2
    )

    # Remove completely empty rows and columns
    df = df.dropna(how="all").dropna(axis=1, how="all")

    # Clean column names
    df.columns = [str(col).strip() for col in df.columns]

    # Save corrected CSV
    output = cleaned / f"{name}.csv"
    df.to_csv(output, index=False)

    print(f"\n{name}")
    print("Rows:", len(df))
    print("Columns:", df.columns.tolist())
    print("Saved:", output)

print("\nALL COUNTY DATA FILES PREPARED")