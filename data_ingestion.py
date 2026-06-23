import os
import pandas as pd
import numpy as np

# Set the path to raw data folder
raw_dir = os.path.join("data", "raw")

print("--- Day 1: Data Ingestion & Quality Report ---")

# List of all raw csv files
files = {
    "01_fund_master": "01_fund_master.csv",
    "02_nav_history": "02_nav_history.csv",
    "03_aum_by_fund_house": "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows": "04_monthly_sip_inflows.csv",
    "05_category_inflows": "05_category_inflows.csv",
    "06_industry_folio_count": "06_industry_folio_count.csv",
    "07_scheme_performance": "07_scheme_performance.csv",
    "08_investor_transactions": "08_investor_transactions.csv",
    "09_portfolio_holdings": "09_portfolio_holdings.csv",
    "10_benchmark_indices": "10_benchmark_indices.csv"
}

loaded_dfs = {}
anomalies_summary = {}

# Loop through and load each CSV
for key, filename in files.items():
    file_path = os.path.join(raw_dir, filename)
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
    
    try:
        df = pd.read_csv(file_path)
        loaded_dfs[key] = df
        
        print("\n" + "#" * 40)
        print(f"File: {filename}")
        print(f"Dimensions: {df.shape}")
        print("Data columns and types:")
        print(df.dtypes)
        print("First 3 rows:")
        print(df.head(3))
        
        # Check for missing values and duplicates
        nulls = df.isnull().sum()
        dupes = df.duplicated().sum()
        anomalies = []
        
        if nulls.sum() > 0:
            for col, count in nulls[nulls > 0].items():
                anomalies.append(f"{count} missing values in '{col}'")
        if dupes > 0:
            anomalies.append(f"{dupes} duplicate rows")
            
        # Quick sanity check on NAV values
        if "nav" in df.columns:
            bad_nav = (df["nav"] <= 0).sum()
            if bad_nav > 0:
                anomalies.append(f"{bad_nav} rows with negative or zero NAV")
                
        if anomalies:
            anomalies_summary[filename] = anomalies
        else:
            anomalies_summary[filename] = ["No anomalies found"]
            
    except Exception as e:
        print(f"Error loading {filename}: {e}")

# Explore Fund Master
if "01_fund_master" in loaded_dfs:
    df_master = loaded_dfs["01_fund_master"]
    print("\n" + "#" * 40)
    print("EXPLORATORY ANALYSIS - FUND MASTER")
    print("#" * 40)
    print("Fund Houses:", df_master["fund_house"].unique())
    print("\nCategories:", df_master["category"].unique())
    print("\nSub-Categories:", df_master["sub_category"].unique())
    print("\nRisk Categories:", df_master["risk_category"].unique())
    
    print("\nAMFI Scheme Code Structure Notes:")
    print("- AMFI codes are unique 5-6 digit numeric IDs for mutual fund schemes in India.")
    print("- Used as the primary key to link scheme details to their historical NAVs.")

# Validate AMFI codes between Master and NAV files
if "01_fund_master" in loaded_dfs and "02_nav_history" in loaded_dfs:
    df_master = loaded_dfs["01_fund_master"]
    df_nav = loaded_dfs["02_nav_history"]
    
    master_codes = set(df_master["amfi_code"].unique())
    nav_codes = set(df_nav["amfi_code"].unique())
    
    missing_nav = master_codes - nav_codes
    missing_master = nav_codes - master_codes
    
    print("\n" + "#" * 40)
    print("AMFI CODE VALIDATION")
    print("#" * 40)
    print(f"Codes in Master: {len(master_codes)}")
    print(f"Codes in NAV History: {len(nav_codes)}")
    print(f"Codes in Master but missing in NAV History: {len(missing_nav)}")
    print(f"Codes in NAV History but missing in Master: {len(missing_master)}")

# Print final quality summary
print("\n" + "#" * 40)
print("DATA QUALITY SUMMARY")
print("#" * 40)
for filename, issues in anomalies_summary.items():
    print(f"{filename}:")
    for issue in issues:
        print(f"  - {issue}")

