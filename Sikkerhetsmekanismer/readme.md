### Generelt
I mappen miljøoppsett finnes dokumentasjon for hvordan Kubernetes-miljøet ble satt opp, hvordan de forskjellige sikkerhetsmekanismene ble implementer og hvordan ytelsestestene ble kjørt.

Under en initiell testrunde ble Grafana brukt til å visualisere ressursbruken til Kubernetes-klusteret. Det finnes en guide for å sette dette opp i miljøoppsett-mappen og bildene som ble produsert ligger i GrafanaBilder-mappen, men disse resultatene ble ikke benyttet i bacheloroppgaven.

### Hvordan parse resultater fra .txt til .csv
Scriptet "parse.py" tar inn 1 .txt fil og skriver den om til .csv format.
For å benytte egne filer må scriptet redigeres slik at filnavnet, som er plassert nederst i scriptet, passer med .txt filen som skal parses.

### Hvordan bruke plot-scriptene
Scriptene "linjediagram.py", "søylediagram.py" og "tabell.py" tar inn 5 csv filer, en for hver av testene, og lager henholdsvis linjediagrammer, søylediagrammer og tabeller (som viser avvik i prosent) ut ifra disse.
For å benytte egne filer må scriptet redigeres slik at filnavnene, som er plassert øverst i scriptet, passer med .csv filene og etikkenene blir passende.
