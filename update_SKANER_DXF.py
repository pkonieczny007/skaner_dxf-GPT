import os
import fdxf
import pandas as pd
import time
from datetime import datetime

# Funkcja tworząca plik data z wykazu
def prepare_data(file_path):
    if not os.path.exists("data.csv"):
        if os.path.exists(file_path):
            df = pd.read_excel(file_path)
            df = df[["Nazwa", "Abmess_1", "Abmes_2"]]
            df = df.dropna(subset=["Nazwa"])  # Usuwanie wierszy, gdzie "Nazwa" jest pusta
            df.to_csv("data.csv", index=False)
            print("Plik data utworzony.")
        else:
            print(f"Plik {file_path} nie istnieje. Upewnij się, że jest w katalogu.")

# Funkcja skanowania plików DXF
def scan():
    prepare_data("wykaz.xlsx")
    data = pd.read_csv("data.csv")
    data["Nazwa"] = data["Nazwa"].fillna("")  # Zastąpienie NaN pustymi stringami

    while True:
        dxf_data = []
        latest_file = None
        latest_time = None

        for filename in os.listdir():
            if filename.endswith('.dxf'):
                file_time = os.path.getmtime(filename)
                if latest_time is None or file_time > latest_time:
                    latest_file = filename
                    latest_time = file_time

        if latest_file:
            wys_value = fdxf.wys(latest_file)
            sze_value = fdxf.sze(latest_file)
            date = time.ctime(latest_time)
            date_time_obj = datetime.strptime(date, "%a %b %d %H:%M:%S %Y")

            # Wyodrębnienie nazwy dla porównania
            base_name = "_".join(latest_file.split("_")[:4])
            match = data[data["Nazwa"].str.startswith(base_name)]

            if not match.empty:
                abmess_1 = match.iloc[0]["Abmess_1"]
                abmess_2 = match.iloc[0]["Abmes_2"]

                if (wys_value in [abmess_1, abmess_2] and
                    sze_value in [abmess_1, abmess_2]):
                    status = "Pasuje"
                    scale = None
                else:
                    scale = max(abmess_1, abmess_2) / max(wys_value, sze_value)
                    status = "Skala różna"

                result = {
                    "Nazwa": latest_file,
                    "Wysokość": wys_value,
                    "Szerokość": sze_value,
                    "Abmess_1": abmess_1,
                    "Abmess_2": abmess_2,
                    "Status": status,
                    "Skala": scale
                }
            else:
                result = {
                    "Nazwa": latest_file,
                    "Wysokość": wys_value,
                    "Szerokość": sze_value,
                    "Status": "Brak w wykazie"
                }

            dxf_data.append(result)

        for item in dxf_data:
            print(item)

        repeat = input("Naciśnij Enter, aby powtórzyć skanowanie, lub wpisz 'c', aby wyczyścić ekran: ").lower()
        if repeat == "c":
            os.system('cls' if os.name == 'nt' else 'clear')

# Uruchomienie skanera
scan()

print("Dziękuję i zapraszam ponownie!")
