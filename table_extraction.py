import pdfplumber
import pandas as pd

pdf_path = r"g:\Aplikacja geodezyjna\Dane do LLM\Dz.U. poz.219.pdf"
output_dir = r"g:\Aplikacja geodezyjna\Dane do LLM"

# Tutaj ręcznie definiujesz tabele:
# każdy element to osobny słownik z opisem i zakresem stron.
tabele_do_ekstrakcji = [
    {"opis": "Zaliczanie gruntów do uzytkow", "start_page": 20, "end_page": 26},
    {"opis": "Atrybuty punktow granicznych", "start_page": 28, "end_page": 29},
    {"opis": "Ograniczenia atrybutowe obiektow", "start_page": 40, "end_page": 45},
    # Dodawaj kolejne tabelki według potrzeb
]

for tabela in tabele_do_ekstrakcji:
    all_tables = []
    with pdfplumber.open(pdf_path) as pdf:
        for i in range(tabela["start_page"], tabela["end_page"]):
            page = pdf.pages[i]
            tables = page.extract_tables()
            if tables:
                for tab_idx, table in enumerate(tables, 1):
                    df = pd.DataFrame(table)
                    output_file = f"{output_dir}/{tabela['opis'].replace(' ', '_')}_strona_{i+1}_tabela_{tab_idx}.csv"
                    df.to_csv(output_file, index=False, encoding="windows-1250")
                    all_tables.append(df)

    # Opcjonalnie: jeden zbiorczy CSV dla danej tabeli
    if all_tables:
        merged = pd.concat(all_tables, ignore_index=True)
        merged.to_csv(f"{output_dir}/{tabela['opis'].replace(' ', '_')}_calosc.csv", 
                      index=False, encoding="windows-1250")

    print(f"Tabela '{tabela['opis']}' ze stron {tabela['start_page']+1}-{tabela['end_page']} zapisana!")

print("Ekstrakcja wszystkich wskazanych tabel zakończona.")
