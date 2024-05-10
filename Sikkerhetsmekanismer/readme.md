### Generelt
I mappen miljøoppsett finnes dokumentasjon for hvordan Kubernetes-miljøet ble satt opp og hvordan de forskjellige sikkerhetsmekanismene ble implementert.

Under en initiell testrunde ble Grafana brukt til å visualisere ressursbruken til klusteret. Det finnes også en guide for å sette dette opp i miljøoppsett-mappen og bildene som ble produsert ligger i GrafanaBilder-mappen, men disse resultatene ble ikke benyttet i bacheloroppgaven.

### Hvordan parse resultater fra .txt til .csv
Scriptet "parse.py" tar inn 1 .txt fil og skriver den om til .csv format.
For å benytte egne filer må scriptet redigeres slik at filnavnet, som er plassert nederst i scriptet, passer med .txt filen som skal parses.

### Hvordan bruke plot-scriptene
Scriptene "linjediagram.py", "søylediagram.py" og "tabell.py" tar inn 5 csv filer, en for hver av testene, og lager henholdsvis linjediagrammer, søylediagrammer og tabeller ut ifra .csv filene.
For å benytte egne filer må scriptet redigeres slik at filnavnene, som er plassert øverst i scriptet, passer med .csv filene og etikkenene blir passende.
