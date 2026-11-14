from pathlib import Path
import pandas as pd

base = Path.home() / "OneDrive" / "Desktop" / "Kenya County Budget Intelligence"
folder = base / "Data" / "Processed"

for file in folder.glob("*_long.csv"):

    df = pd.read_csv(file)

    missing = df[df["Amount"].isna()]

    print(f"\n--- {file.name} ---")
    print("Missing records:", len(missing))

    if not missing.empty:
        print(
            missing[["Code", "County", "Financial_Year"]]
            .to_string(index=False)
        )

print("\nMISSING DATA REVIEW COMPLETE")