import os

# Wenn der Code in einem normalen Python-Programm ausgeführt wird.
if ("__file__" in vars()):
    #Aktuellen Pfad herausfinden ("__file__") zeigt auf die Programmdatei incl. Pfad
    path, filename = os.path.split(os.path.abspath(__file__))
    #  Jetzt einen neuen Dateinamen damit verbinden
    dateiname = os.path.join(path,"LogVol.dat")
    dateinamenew = os.path.join(path,"LogVolResults.dat")
    print(dateiname)
# Beim Jupyter-Notebook ist der Dateiname ausreichend
else:
    dateiname = ("LogVol.dat")
    dateinamenew = ("LogVolResults.dat")
    print (dateiname)

try:
    with  open(dateinamenew,"w") as dateinew:
        
        datei = open(dateiname,"r")
        for zeile in datei:
            bezeichnung = zeile[0:10]
            name = zeile[10:20]
            groesseinmb = zeile[20:29]
            freespace = zeile[30:38]

            prozent = 100 - int(freespace) * 100 / int(groesseinmb)
            
            if(prozent >= 80.0):
                dateinew.write(f"{name}{bezeichnung}Auslastung: {prozent}%\n")
                
            
    datei.close()
except Exception as e: 
    print (f"Fehler beim Lesen der Datei {dateiname}")
    print(e)
    if datei:
        datei.close()

