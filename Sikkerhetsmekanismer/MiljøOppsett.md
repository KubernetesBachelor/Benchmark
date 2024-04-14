##Forutsetninger
Minikube 
Kubectl  
##Helm
'''
curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
chmod 700 get_helm.sh
./get_helm.sh
'''
##Prometheus
'''
helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
helm repo update
helm install prometheus prometheus-community/prometheus
kubectl expose service prometheus-server --type=NodePort --target-port=9090 --name=prometheus-server-ext
minikube service prometheus-server-ext
'''
##Grafana
'''
helm repo add grafana https://grafana.github.io/helm-charts 
helm repo update
helm install grafana grafana/grafana
kubectl expose service grafana --type=NodePort --target-port=3000 --name=grafana-ext
minikube service grafana-ext
'''
Bruk følgende kommando for å hente passord til Grafana, brukernavnet er "admin"
'''
kubectl get secret --namespace default grafana -o jsonpath="{.data.admin-password}" | ForEach-Object { [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($_)) }
'''
Videre ble prometheus lagt til som datakilde ved å tilknytte IP'en som ble gitt når prometheus sin service ble eksponert.
Grafana ble satt opp med dashboard Node Exporter, ID:1860
