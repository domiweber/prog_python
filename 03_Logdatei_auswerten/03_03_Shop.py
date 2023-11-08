import os

# Wenn der Code in einem normalen Python-Programm ausgeführt wird.
if ("__file__" in vars()):
    #Aktuellen Pfad herausfinden ("__file__") zeigt auf die Programmdatei incl. Pfad
    path, filename = os.path.split(os.path.abspath(__file__))
    #  Jetzt einen neuen Dateinamen damit verbinden
    dateiname = os.path.join(path,"ppDaten.csv")
    print(dateiname)
# Beim Jupyter-Notebook ist der Dateiname ausreichend
else:
    dateiname = ("ppDaten.csv")
    print (dateiname)


hoechsterUmsatz = [0,"",0] 
niedrigsterUmsatz = [0,"",0] 
gesamtUmsatz = 0
umsatzmini = 0
umsatzmidi = 0
umsatzmaxi = 0

try:
    datei = open(dateiname,"r") 
    for zeile in datei:
        # jetzt die Zeile in Spalten teilen. Das kennen Sie ja schon
        spalten = zeile.strip().split(";")
        #Höchsten Umsatz Bestimmen
        if(int(spalten[2])> hoechsterUmsatz[2]):
            hoechsterUmsatz = [int(spalten[0]),spalten[1],int(spalten[2])]
        #Niedrigsten Umsatz bestimmen
        if(int(spalten[2])< hoechsterUmsatz[2]):
            niedrigsterUmsatz = [int(spalten[0]),spalten[1],int(spalten[2])]
        #Gesamtumsatz bestimmen
        gesamtUmsatz = gesamtUmsatz + int(spalten[2])

        #Umsatz je Marktart
        if(int(spalten[0]) == 1):
            umsatzmini = umsatzmini + int(spalten[2])
        elif(int(spalten[0]) == 2):
            umsatzmidi = umsatzmidi + int(spalten[2])
        elif(int(spalten[0]) == 3): 
            umsatzmaxi = umsatzmaxi + int(spalten[2])   
        
       
    datei.close()
except Exception as e: 
    print (f"Fehler beim Lesen der Datei {dateiname}")
    print(e)
    if datei:
        datei.close()


#Ausgabe

print("Auswertung\n-----------------------")
print(f"Pächter mit dem höchsten Umsatz...\nName: {hoechsterUmsatz[1]}\nUmsatz: {hoechsterUmsatz[2]} EURO\n")
print(f"Pächter mit dem niedrigsten Umsatz...\nName: {niedrigsterUmsatz[1]}\nUmsatz: {niedrigsterUmsatz[2]} EURO\n")
print(f"Der Gesamtzumsatz: {gesamtUmsatz} EURO teilt sich auf in:\n----------------------------------------------\n")
print(f"Mini-Shop: {umsatzmini} EURO / Anteil am Gesamtzumsatz: {round(umsatzmini *100 / gesamtUmsatz,2)}%")
print(f"Midi-Shop: {umsatzmidi} EURO / Anteil am Gesamtzumsatz: {round(umsatzmidi *100 / gesamtUmsatz,2)}%")
print(f"Maxi-Shop: {umsatzmaxi} EURO / Anteil am Gesamtzumsatz: {round(umsatzmaxi *100 / gesamtUmsatz,2)}%")
