
import pdfplumber
import gspread
from oauth2client.service_account import ServiceAccountCredentials

pdf_path = "sample_table_data.pdf"
with pdfplumber.open(pdf_path) as pdf:
    page = pdf.pages[0]
    table = page.extract_table()

scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
client = gspread.authorize(creds)

sheet = client.open("Automated Payroll Sheet Rehan").sheet1
sheet.clear()
for row in table:
    sheet.append_row(row)
