## Performing the performance test
The "stress_test.sh" Bash script runs the performance tests using the tools Sysbench and Fio. The script is referenced in "Dockerfile" to build a Docker image named "stresstest:v1", which is then used to run a Kubernetes Job defined in the file "stresstest-job.yaml"

Command to build the image and deploy the Job
```
eval $(minikube docker-env)
sudo docker build -t stresstest:v1 .
kubectl apply -f stresstest-job.yaml
```
After running the script, the results can be retrieved be checking the logs of the pod named "stresstest-<PodID>.
Command to read the logs:
```
kubectl log <pod-ID> -n stresstest
```
## Implementing security features
All components in the Kubernetes cluster are placed in a namespace called "stresstest". This documentation includes two different .yaml files that create a namespace with this name. The file "namespace.yaml" creates a default namespace and is used when Po Security Admission is not enabled. If "namespace.yaml" has already been implemented, it must be deleted before deploying Pod Security Admission, as borht define the same namespace.

### Pod Security Admission
Pod Security Admission is added by applying Pod Security Standards to a namespace.
The file "PSA-namespace.yaml" creates a namepsace named "stresstes" with PSA enabled. This namespace is used for all performance testing involing PSA.

Command to implement Pod Security Admission
```
kubectl apply -f PSA-namespace.yaml
```

### Auditing
Auditing must be configured to start along with the cluster. It's sufficient to stop and restart Minikube with the correct configuration. prometheus and Grafana will continue to function as usual after a restart.

Commands to enable audit policy "audit-policy.yaml".
```
mkdir -p ~/.minikube/files/etc/ssl/certs
cp audit-policy.yaml ~/.minikube/files/etc/ssl/certs/
minikube start --extra-config=apiserver.audit-policy-file=/etc/ssl/certs/audit-policy.yaml --extra-config=apiserver.audit-log-path=-
```

### Role Based Access Control
To apply RBAC to a Kubernetes Job, you need a Service Acount to bind RBAC rules to the Job.
An example is provied in "job-SA.yaml".
RBAC is configured by defining a Role that specifies permissions, and a Role Binding that binds those permission to a namespace (in this example).

Role is created in "job-role.yaml" <br />
RoleBinding is created in "job-rolebinding.yaml" <br />
<br />
Commands to apply RBAC:
```
kubectl apply -f job-SA.yaml
kubectl apply -f job-role.yaml
kubectl apply -f job-rolebinding.yaml
```

## Setting up Grafana
Below is the process used to set up Prometheus and Grafana in the Kubernetes cluster.
### Requirements <br />
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
Use the following command to retrieve the Grafana "admin" passwordB
```
kubectl get secret --namespace default grafana -o jsonpath="{.data.admin-password}" | ForEach-Object { [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($_)) }
```
Prometheus was then added as a data source in Grafana by using the IP address provided when exposing the Prometheus service.
Grafana was configured with the dashboard Node Exporter, ID:1860

### Sources
[Denne Guiden](https://medium.com/@gayatripawar401/deploy-prometheus-and-grafana-on-kubernetes-using-helm-5aa9d4fbae66) ble fulgt for å sette opp Grafana og Prometheus <br />
