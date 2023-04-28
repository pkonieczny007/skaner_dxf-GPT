import os 
import fdxf
import time
from datetime import datetime

def scan():
    stan = 1
    while stan != 'nie':
        dxf_date=[]
        n=0
        for filename in os.listdir():
            if filename.endswith('.dxf'):
                a={}
                n+=1
                wys=fdxf.wys(filename)
                szer=fdxf.sze(filename)
                date = time.ctime(os.path.getmtime(filename))
                date_time_obj = datetime.strptime(date, "%a %b %d %H:%M:%S %Y")
                b = [date_time_obj, filename, wys, szer]
                dxf_date.append(b)
        
        dxf_date.sort(reverse=True)
        print(dxf_date[0])
        stan = input('czy chcesz powtorzyc skanowanie? c -> clear screen ')
        if stan == 'c':
            os.system('cls')
        else:
            continue
    return dxf_date

scan()    

print('dziekuje i zapraszam ponownie;')
