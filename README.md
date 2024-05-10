### Baseline
Denne mappen inneholder guider for hvordan miljøene til Vertsmaskin, VM, Konteiner og Kubernetes ble satt opp og hvordan ytelsestestene ble kjørt

### Sikkerhetesmekanismer
Denne mappen inneholder guider for hvordan de ulike sikkerhetesmekanismene ble implementert i Kubernetes klusteret, sammen med alle konfigurasjonsfilene. I tillegg ligger scriptene for å kunne lage grafer og tabeller fra resultatene. Grafana ble brukt for å overvåke ressuresene i klusteret underveis og oppsett og bilder fra dette ligger også i denne mappen.



# Hvordan sette opp og kjøre scriptet
Først lager du Dockerfile

Deretter lager du shell scriptet

Gjør shell scriptet kjørbart med følgende kommando "chmod +x shell_script.sh"

Deretter bygger du et docker image med følgende kommando "sudo docker build -t <Navn_til_konteiner> ."

Deretter kan du kjøre konteineren "sudo docker run -v /path_to_script:/path_where_script_shall_run_in_container"

Når du har fått resultatfilen så kan du kjøre formatering scriptet som vil gi deg bilder av grafene som produseres
