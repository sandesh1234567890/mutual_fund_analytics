import requests
import pandas as pd
import os

raw_dir = os.path.join("data", "raw")
os.makedirs(raw_dir, exist_ok=True)

# 1. Fetch live NAV for HDFC Top 100 Direct (125497)
hdfc_code = "125497"
url_hdfc = f"https://api.mfapi.in/mf/{hdfc_code}"

print(f"Fetching NAV data for HDFC Top 100 Direct ({hdfc_code})...")
try:
    response = requests.get(url_hdfc, timeout=15)
    response.raise_for_status()
    data = response.json()
    
    # Save the NAV data
    df_hdfc = pd.DataFrame(data["data"])
    df_hdfc["amfi_code"] = hdfc_code
    output_path = os.path.join(raw_dir, "nav_history.csv")
    df_hdfc.to_csv(output_path, index=False)
    print(f"Saved HDFC NAV history to {output_path} ({len(df_hdfc)} records)")
except Exception as e:
    print(f"Failed to fetch HDFC NAV: {e}")

# 2. Fetch NAV for the 5 key schemes
key_schemes = {
    "119551": "SBI Bluechip",
    "120503": "ICICI Bluechip",
    "118632": "Nippon Large Cap",
    "119092": "Axis Bluechip",
    "120841": "Kotak Bluechip"
}

print("\nFetching NAV data for 5 key schemes...")
for code, name in key_schemes.items():
    url = f"https://api.mfapi.in/mf/{code}"
    print(f"Fetching {name} ({code})...")
    try:
        res = requests.get(url, timeout=15)
        res.raise_for_status()
        data = res.json()
        
        df = pd.DataFrame(data["data"])
        df["amfi_code"] = code
        out_file = os.path.join(raw_dir, f"{code}.csv")
        df.to_csv(out_file, index=False)
        print(f"Saved {name} NAV to {out_file} ({len(df)} records)")
    except Exception as e:
        print(f"Failed to fetch {name} ({code}): {e}")

