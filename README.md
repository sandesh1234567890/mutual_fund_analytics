# Capstone Project I - Mutual Fund Analytics

This project involves the ingestion, validation, and analytics of mutual fund datasets.

## Folder Structure
- **data/raw**: Raw CSV datasets and fetched live NAV records
- **data/processed**: Cleaned data tables
- **notebooks**: Jupyter notebooks for EDA and performance computations
- **sql**: SQLite database schemas and analysis queries
- **dashboard**: Power BI dashboard templates
- **reports**: Generated charts, presentation slide decks, and summaries

## How to Run Scripts

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run Data Ingestion & Quality Analysis**:
   ```bash
   python data_ingestion.py
   ```

3. **Fetch Latest Live NAV Data**:
   ```bash
   python live_nav_fetch.py
   ```
