### Hvordan formattere og plotte CPU grafene
Benytt parse_txt_til_csv.py for å omgjøre en og en resultatfil fra hvert system til sin egen .csv fil.
parse_txt_til_csv.py krever at det ligger filer med navn Resultater.txt i samme mappe som skriptet kjøres fra.

PlotScriptCPU.py tar inn 4 .csv filer med navn "parset_cpu_resultater_Konteiner.csv", "parset_cpu_resultater_VM.csv", "parset_cpu_resultater_Native.csv" og "parset_cpu_resultater_Kubernetes.csv" og bruker disse for å produsere en figur med fire grafer.

### Hvordan plott Minne og Disk grafene
DiskScript.py og MinneScript.py tar inn 4 .txt filer produsert fra shell scriptet og bruker disse for å produsere en figur hver med fire søyler.
Navnene på filene må være følgende: 'VMResultater.txt', 'KubernetesResultater.txt', 'NativeResultater.txt' og 'KonteinerResultater.txt'
