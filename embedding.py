import re

txt_path = r"g:\Aplikacja geodezyjna\Dane do LLM\Dz.U. poz.219.txt"

with open(txt_path, encoding="utf-8") as f:
    tekst = f.read()

# Szukamy paragrafów rozpoczynających się od § + numer
paragrafy = [p.strip() for p in re.split(r'\n?§\s?\d+[a-zA-Z]?\.', tekst) if len(p.strip()) > 40]
idx = tekst.find("§ 1.")  # lub innego pierwszego paragrafu
wstep = tekst[:idx]
akapity_wstepu = [a.strip() for a in wstep.split('\n\n') if len(a.strip()) > 40]
print(f"Znaleziono {len(akapity_wstepu)} akapitów wstępu do embeddingów!")
fragmenty = akapity_wstepu + paragrafy
print(f"Znaleziono {len(fragmenty)} fragmentów do embeddingów!")
