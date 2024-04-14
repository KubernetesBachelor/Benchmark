### Hvordan formattere og plotte CPU grafene
Benytt parse_txt_til_csv.py for å omgjøre en og en resultatfil fra hvert system til sin egen .csv fil.
parse_txt_til_csv.py krever at det ligger filer med navn Resultater.txt i samme mappe som skriptet kjøres fra.

PlotScriptCPU.py tar inn 4 .csv filer og bruker disse for å produsere en figur med fire grafer.


### Hvordan plott Minne og Disk grafene
DiskScript.py og MinneScript.py tar inn 4 .txt filer produsert fra shell scriptet og bruker disse for å produsere en figur hver med fire søyler.
