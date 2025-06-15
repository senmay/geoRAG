import fitz
import re
import pandas as pd

pdf_path = r"g:\Aplikacja geodezyjna\Dane do LLM\Dz.U. poz.219.pdf"
output_file = r"g:\Aplikacja geodezyjna\Dane do LLM\ekstrakt_formularz.csv"

start_page = 40  # przykład: ustaw na stronę z formularzową tabelą
end_page = 46    # wyciągnij zakres stron, gdzie są takie bloki

records = []

doc = fitz.open(pdf_path)
for i in range(start_page, end_page):
    text = doc[i].get_text("text")

    # Znajdź wszystkie bloki zaczynające się od "Nazwa:" i kończące na następnym "Nazwa:" lub koniec tekstu
    pattern = r"Nazwa:(.*?)(?=Nazwa:|$)"
    blocks = re.findall(pattern, text, re.DOTALL)

    for block in blocks:
        # Wyciągnij pola przez regexy
        nazwa = re.search(r"^\s*(\S+)", block)
        jezyk = re.search(r"Język naturalny:(.*?)(OCL:|$)", block, re.DOTALL)
        ocl = re.search(r"OCL:(.*)", block, re.DOTALL)
        records.append({
            "Nazwa": nazwa.group(1).strip() if nazwa else "",
            "Język naturalny": jezyk.group(1).strip() if jezyk else "",
            "OCL": ocl.group(1).strip() if ocl else "",
        })

# Zamień na DataFrame i zapisz do CSV
df = pd.DataFrame(records)
df.to_csv(output_file, index=False, encoding="utf-8")

print("Wyciągnięto formularzowe bloki do CSV!")
