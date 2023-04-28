

def sze(filename):
    with open(filename) as file_obj:
        file=file_obj.read()
        lista = file.split()

    min_index= lista.index('$EXTMIN')
    max_index=lista.index('$EXTMAX')

    minx_index=min_index + 2
    maxx_index=max_index +2

    minX=float(lista[minx_index])
    maxX=float(lista[maxx_index])

    miny_index=min_index + 4
    maxy_index=max_index +4          

    minY=float(lista[miny_index])
    maxY=float(lista[maxy_index])

    szerokosc=int(maxX)-int(minX)

    return szerokosc




def wys(filename):
    with open(filename) as file_obj:
        file=file_obj.read()
        lista = file.split()

    min_index= lista.index('$EXTMIN')
    max_index=lista.index('$EXTMAX')

    minx_index=min_index + 2
    maxx_index=max_index +2

    minX=float(lista[minx_index])
    maxX=float(lista[maxx_index])

    miny_index=min_index + 4
    maxy_index=max_index +4          

    minY=float(lista[miny_index])
    maxY=float(lista[maxy_index])

    wysokosc=int(maxY)-int(minY)

    return wysokosc








		




