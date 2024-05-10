### Baseline
Denne mappen inneholder dokumentasjon for hvordan ytelsestestene for vertsmaskin, konteiner, VM og Kubernetes ble gjennomført.
Vedlagt ligger dokumentasjon og intsallasjonsguide for hvordan de ulike miljøene ble satt opp.
I tillegg ligger ytelsestesten og guide til hvordan testene ble kjørt.

### Sikkerhetesmekanismer
Denne mappen inneholder dokumentasjon for hvordan Kubernetes sin ytelse ble målt ved implementering av ulike sikkerhetsmekanismer.
Vedlagt ligger konfigurasjonsfiler for de ulike sikkerhetsmekanismene og hvordan de ble implementert.
Sammen med dette ligger hvordan scriptet ble kjørt for å teste ytelsen.

Grafana ble brukt for å overvåke ressuresene i klusteret underveis og oppsett og bilder fra dette ligger også i denne mappen.



# Hvordan sette opp og kjøre scriptet
Først lager du Dockerfile

Deretter lager du shell scriptet

Gjør shell scriptet kjørbart med følgende kommando "chmod +x shell_script.sh"

Deretter bygger du et docker image med følgende kommando "sudo docker build -t <Navn_til_konteiner> ."

Deretter kan du kjøre konteineren "sudo docker run -v /path_to_script:/path_where_script_shall_run_in_container"

Når du har fått resultatfilen så kan du kjøre formatering scriptet som vil gi deg bilder av grafene som produseres
