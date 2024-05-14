from ubuntu:latest
#Oppdaterer etter siste pakker fra Ubuntu og laster ned sysbench & fio
RUN apt-get update && \
         apt-get install -y sysbench && \
         apt-get install -y fio

#For å definere hvor konteineren skal starte
WORKDIR /app/

#Lager mappen som resultatet blir lagret i senere
RUN mkdir -p /app/data

#Legge inn skriptet i konteineren
ADD stress_test.sh /app/stress_test.sh

#Gjør skriptet kjørbart
RUN chmod +x /app/stress_test.sh

#Kjøre skriptet ved oppstart av konteiner
CMD ["/app/stress_test.sh"]
