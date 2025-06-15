import pdfplumber

# Ścieżki do plików
pdf_path = r"g:\Aplikacja geodezyjna\Dane do LLM\Dz.U. poz.219.pdf"
txt_path = r"g:\Aplikacja geodezyjna\Dane do LLM\Dz.U. poz.219.txt"

with pdfplumber.open(pdf_path) as pdf:
    all_text = ""
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:
            all_text += page_text + "\n"

# Zapisz tekst do pliku .txt
with open(txt_path, "w", encoding="utf-8") as f:
    f.write(all_text)

print(f"Tekst wyciągnięty z PDF i zapisany jako {txt_path}!")
# Informacja o zakończeniu
print("Proces zakończony pomyślnie.")