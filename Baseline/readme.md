## Performing the performance test
The "stress_test.sh" Bash script runs the performance tests using the tools Sysbench and Fio. The script is referenced in "Dockerfile" to build a Docker image named "stresstest:v1", which is then used to run a Kubernetes Job defined in the file "stresstest-job.yaml"

### Command to build the image and deploy the Job
```
eval $(minikube docker-env)
sudo docker build -t stresstest:v1 .
kubectl apply -f stresstest-job.yaml
```
After running the script, the results can be retrieved be checking the logs of the pod named "stresstest-<pod-ID>". Command to read the logs:
```
kubectl log <pod-ID> -n stresstest
```
##How to parse results from .txt to .csv
The script "parse.py" takes a single .txt file as input and converts it to .csv format. 
To use custom files, the script must be edited so that the filename located at the bottom matches the .txt file you want to parse.

##How to use the plotting scripts
The scripts "linjediagram.py" and "søylediagram.py" take 5 csv files, one for each of the tests, and generates line charts, bar charts and tables with percentage deviation, respectively. To use custom files, you must edit the script so the filenames, defined at the top, matches you .csv files and change the labels accordingly.

## Host machine specifications
- RAM: 8GB
- CPU: Intel(R) Core(TM)i7-8550U CPU@ 1.80GHz
- Lagring: SSD: LITEON CV1-DB256, 256GB
- serie nr: SD0J21064L1TH59105X5
- OS: Ubuntu 22.04.4

## Virtual machine specifications
- RAM: 4GB
- 1x prosessor, 4 kjerner
- hard disk (SCSI): 64GB
- OS: Windows 11 home
- I/O controller: LSI Logic SAS
- Disk type: SATA

## Container Setup
### Install Docker
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
### Build image
```
sudo docker build -t <Navn_til_konteiner> .
```
### Run container
```
sudo docker run -v /home/ubuntu/docker_2/docker_assignment:/app konteiner
```
## Kubernetes setup
### Intall Kubectl
```
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
kubectl version --client
```
### Install Docker
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
### Install Minikube
```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```
### Build image
```
eval $(minikube docker-env)
docker build -t stresstest:v1 .
```
## Build Pod
```
kubectl apply -f stresstest-job.yaml
```
