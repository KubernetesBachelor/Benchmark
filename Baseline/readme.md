## Performing the performance test
The "stress_test.sh" Bash script runs the performance tests using the tools Sysbench and Fio. The script is referenced in "Dockerfile" to build a Docker image named "stresstest:v1", which is then used to run a Kubernetes Job defined in the file "stresstest-job.yaml"

### Command to build the image and deploy the Job
```
eval $(minikube docker-env)
sudo docker build -t stresstest:v1 .
kubectl apply -f stresstest-job.yaml
```
After running the script, the results can be retrieved be checking the logs of the pod named "stresstest-. Command to read the logs:
```
kubectl log <pod-ID> -n stresstest
```
## Hvordan parse resultater fra .txt til .csv
Scriptet "parse.py" tar inn 1 .txt fil og skriver den om til .csv format.
For å benytte egne filer må scriptet redigeres slik at filnavnet, som er plassert nederst i scriptet, passer med .txt filen som skal parses.

## Hvordan bruke plot-scriptene
Scriptene "linjediagram.py" og "søylediagram.py" tar inn 4 csv filer, en for hver av testene, og lager henholdsvis linjediagrammer, søylediagrammer og tabeller ut ifra disse.
For å benytte egne filer må scriptet redigeres slik at filnavnene, som er plassert øverst i scriptet, passer med .csv filene og etikkenene blir passende.


## Vertsmaskin oppsett
- RAM: 8GB
- CPU: Intel(R) Core(TM)i7-8550U CPU@ 1.80GHz
- Lagring: SSD: LITEON CV1-DB256, 256GB
- serie nr: SD0J21064L1TH59105X5
- OS: Ubuntu 22.04.4

## Virtuell maskin oppsett
- RAM: 4GB
- 1x prosessor, 4 kjerner
- hard disk (SCSI): 64GB
- OS: Windows 11 home
- I/O controller: LSI Logic SAS
- Disk type: SATA

## Konteiner oppsett
### Installer Docker
```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo docker run hello-world
```
### Bygge image
```
sudo docker build -t <Navn_til_konteiner> .
```
### Kjøre konteiner
```
sudo docker run -v /home/ubuntu/docker_2/docker_assignment:/app konteiner
```
## Kubernetes oppsett
### Intaller Kubectl
```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
kubectl version --client
```
### Installer Docker
```
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Add the repository to Apt sources:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update

sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

sudo docker run hello-world
```
### Installer Minikube
```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```
### Bygge image
```
eval $(minikube docker-env)
docker build -t stresstest:v1 .
```
## Bygge Pod
```
kubectl apply -f stresstest-job.yaml
```
