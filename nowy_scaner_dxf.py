import os
import time

def sze(filename):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as file_obj:
        file = file_obj.read()
        lista = file.split()

    min_index = lista.index('$EXTMIN')
    max_index = lista.index('$EXTMAX')

    minx_index = min_index + 2
    maxx_index = max_index + 2

    minX = float(lista[minx_index])
    maxX = float(lista[maxx_index])

    miny_index = min_index + 4
    maxy_index = max_index + 4          

    minY = float(lista[miny_index])
    maxY = float(lista[maxy_index])

    szerokosc = int(maxX) - int(minX)

    return szerokosc

def wys(filename):
    with open(filename, 'r', encoding='utf-8', errors='ignore') as file_obj:
        file = file_obj.read()
        lista = file.split()

    min_index = lista.index('$EXTMIN')
    max_index = lista.index('$EXTMAX')

    minx_index = min_index + 2
    maxx_index = max_index + 2

    minX = float(lista[minx_index])
    maxX = float(lista[maxx_index])

    miny_index = min_index + 4
    maxy_index = max_index + 4          

    minY = float(lista[miny_index])
    maxY = float(lista[maxy_index])

    wysokosc = int(maxY) - int(minY)

    return wysokosc

def scan():
    stan = 'tak'
    while stan.lower() != 'nie':
        dxf_list = []
        dxf_date = []
        for filename in os.listdir():
            if filename.endswith('.dxf'):
                wysokosc = wys(filename)  # Zmieniono nazwę zmiennej
                szerokosc = sze(filename)  # Zmieniono nazwę zmiennej
                date = time.ctime(os.path.getmtime(filename))
                b = [date, filename, wysokosc, szerokosc]
                dxf_date.append(b)

        if dxf_date:
            dxf_date.sort()
            print(dxf_date[-1])
        else:
            print("Brak plików DXF w bieżącym katalogu.")

        stan = input('Czy chcesz powtórzyć skanowanie? (tak/nie/c -> clear screen) ')
        if stan.lower() == 'c':
            os.system('cls')
        else:
            continue

    return dxf_list

scan()

print('Dziękuję i zapraszam ponownie!')

