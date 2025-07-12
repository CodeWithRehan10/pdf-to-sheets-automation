
# 🧾 PDF to Google Sheets Automation

This project automatically extracts **table data from a PDF** using `pdfplumber` and uploads it to **Google Sheets** using the `gspread` library.

## 📂 Files Included
- `main.py`: The main script for extraction and uploading
- `sample_table_data.pdf`: A demo PDF with tabular data
- `requirements.txt`: Required Python packages

## 🚀 How to Run

1. Install required packages:
```bash
pip install -r requirements.txt
```

2. Add your `credentials.json` file (Google service account key)

3. Run:
```bash
python main.py
```

## 🛠 Tech Used
- Python
- pdfplumber
- gspread
- Google Sheets API

## 🔐 Note
Make sure your Google Sheet is **shared with your service account email** (with Editor access).

## 📷 Screenshot Example

| Name   | Department | Salary |
|--------|------------|--------|
| Ali    | HR         | 50,000 |
| Sara   | Finance    | 60,000 |
| Rehan  | IT         | 70,000 |
