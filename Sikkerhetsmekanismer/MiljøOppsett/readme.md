## Gjennomføre ytelsestest
"stress_test.sh" er bash scriptet som gjennomfører ytelsestestene ved å bruke verktøyene sysbench og fio. Scriptet blir benyttet i "Dockerfile" for å lage et image med navn "stresstest:v1". Dette Docker imaget blir brukt for å kjøre en Kubernetes-Job ut ifra filen "stresstest-job.yaml".
Kommando for å bygge imaget og iversette Job'en
```
eval $(minikube docker-env)
sudo docker build -t stresstest:v1 .
kubectl apply -f stresstest-job.yaml
```
Etter at scriptet har kjørt ferdig vil resultatene kunne blitt hentet ut ved sjekke loggene til poden som har navn "stresstest-podID".
Kommando for å lese logger
```
kubectl log <pod-ID> -n stresstest
```
## Implementering av sikkerhetsfunskjoner
Alle komponentene i Kubernetes-klusteret blir plassert i et namespace med navn "stresstest". I denne dokumentasjonen finnes det to forskjellige .yaml filer som lager et namespace med samme navn, "stresstest". .yaml filen med navn "namespace.yaml" lager et default namespace og blir implementert hvis man ikke skal benytte Pod Security Admission. Hvis man skal benytte Pod Security Admission og "namespace.yaml" har blitt deployert må man slette dette namespace før Pod Security Admission kan bli implementert.

### Pod Security Admission
Pod Security Admission blir lagt til ved å sette Pod Security Standarder til et namespace. <br />
"PSA-namespace.yaml" vil lage et nytt namespace med navn "stresstest" som benytter Pod Security Admission. Dette nye namespacet benyttes til alt som omhandler disse ytelsestestene.
Kommandoer for å implementere Pod Security Admission
```
kubectl apply -f PSA-namespace.yaml
```

### Auditing
Auditing må bli configurert til å starte med klusteret. Det holder med å kjøre "minikube stop" for så å starte med rette konfigurasjoner, ved ny oppstart vil Prometheus og Grafana fungere som normalt. <br />
Ved å kjøre følgende kommandoer vil audity policyen "audit-policy.yaml" bli iverksatt.
```
mkdir -p ~/.minikube/files/etc/ssl/certs
cp audit-policy.yaml ~/.minikube/files/etc/ssl/certs/
minikube start --extra-config=apiserver.audit-policy-file=/etc/ssl/certs/audit-policy.yaml --extra-config=apiserver.audit-log-path=-
```

### Role Based Access Control
For å iverksette Role Based Access Control til en Job i Kubernetes vil du trenge en Service Account for å binde RBAC-reglene til Job'en <br />
Et eksempel på en slik Service Account er laget i "job-SA.yaml" <br />
En RBAC settes opp ved å lage en Role som inneholder hvilke rettigheter en skal ha tilgjengelig, og en Role Binding som knytter rettighetene til et Namespace (i dette tilfellet). <br />
Role er laget i "job-role.yaml" <br />
RoleBinding er laget i "job-rolebinding.yaml" <br />
<br />
Kommandoer for å iverksette RBAC
```
kubectl apply -f job-SA.yaml
kubectl apply -f job-role.yaml
kubectl apply -f job-rolebinding.yaml
```

## Sette opp Grafana
Under forklares hvordan Prometheus og Grafana ble satt opp i Kubernetes-klusteret
### Forutsetninger <br />
Minikube <br />
Kubectl  <br />
### Helm <br />
```
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh 
./get_helm.sh
```
### Prometheus
```
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/prometheus
kubectl expose service prometheus-server --type=NodePort --target-port=9090 --name=prometheus-server-ext
minikube service prometheus-server-ext
```
### Grafana
```
helm repo add grafana https://grafana.github.io/helm-charts 
helm repo update
helm install grafana grafana/grafana
kubectl expose service grafana --type=NodePort --target-port=3000 --name=grafana-ext
minikube service grafana-ext
```
Bruk følgende kommando for å hente passord til Grafana, brukernavnet er "admin"
```
kubectl get secret --namespace default grafana -o jsonpath="{.data.admin-password}" | ForEach-Object { [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($_)) }
```
Videre ble prometheus lagt til som datakilde ved å tilknytte IP'en som ble gitt når prometheus sin service ble eksponert. <br />
Grafana ble satt opp med dashboard Node Exporter, ID:1860

### Kilder
[Denne Guiden](https://medium.com/@gayatripawar401/deploy-prometheus-and-grafana-on-kubernetes-using-helm-5aa9d4fbae66) ble fulgt for å sette opp Grafana og Prometheus <br />
