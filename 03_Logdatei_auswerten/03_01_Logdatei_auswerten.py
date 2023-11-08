import os

# Wenn der Code in einem normalen Python-Programm ausgeführt wird.
if ("__file__" in vars()):
    #Aktuellen Pfad herausfinden ("__file__") zeigt auf die Programmdatei incl. Pfad
    path, filename = os.path.split(os.path.abspath(__file__))
    #  Jetzt einen neuen Dateinamen damit verbinden
    dateiname = os.path.join(path,"LogVol.dat")
    print(dateiname)
# Beim Jupyter-Notebook ist der Dateiname ausreichend
else:
    dateiname = ("LogVol.dat")
    print (dateiname)

try:
    datei = open(dateiname,"r") 
    for zeile in datei:
        bezeichnung = zeile[0:9]
        name = zeile[10:19]
        groesseinmb = zeile[20:28]
        freespace = zeile[29:38]

        prozent = 100 - int(freespace) * 100 / int(groesseinmb)
        if(prozent <= 20.0):
            print(name,bezeichnung,"Auslastung:",prozent,"%")

        
    datei.close()
except Exception as e: 
    print (f"Fehler beim Lesen der Datei {dateiname}")
    print(e)
    if datei:
        datei.close()