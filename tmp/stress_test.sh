#!/bin/bash

echo "Starter stresstesting av konteineren ..."

#Test av CPU - tråder og primtall varierer og hver test utføres 10 ganger

# Definerer array for antall tråder og cpu-max-prime verdier
threads=(1 2)
primes=(10000 20000 30000)

# Ytre løkke for antall tråder
for t in "${threads[@]}"; do
  # Indre løkke for cpu-max-prime verdiene
  for p in "${primes[@]}"; do
    # Kjører testen 10 ganger
    for i in {1..10}; do
      echo "Test $i: Starter CPU-test med ${t} tråd(er) og cpu-max-prime=${p} for 30 sekunder..."
      # Kjører sysbench CPU test med tidsbegrensning
      output=$(sysbench cpu --cpu-max-prime="$p" --threads="$t" --time=30 run)
      # Leser output og filtrerer resultatet
      echo "$output" | grep -E "total time|total number of events"
      echo "Tråder: ${t}, cpu-max-prime=${p}, Test $i fullført"
      echo "--------------------------------------------------"
    done
  done
done

# Minnetest 1 - Lese
echo "Starter minnetest i lesemodus ..."
output=$(sysbench memory --memory-block-size=128M --memory-total-size=1G --memory-oper=read --threads=1 run)
filtered_output=$(echo "$output" | grep -oP "\d+(\.\d+)? MiB transferred \(\d+(\.\d+)? MiB/sec\)" | uniq)
echo "Lese: $filtered_output"
echo "Minnetest i lesemodus fullført."
echo "--------------------------------------------------"

# Minnetest 2 - Skrive
echo "Starter minnetest i skrivemodus ..."
output=$(sysbench memory --memory-block-size=128M --memory-total-size=1G --memory-oper=write --threads=1 run)
filtered_output=$(echo "$output" | grep -oP "\d+(\.\d+)? MiB transferred \(\d+(\.\d+)? MiB/sec\)" | uniq)
echo "Skrive: $filtered_output"
echo "Minnetest i skrivemodus fullført."
echo "--------------------------------------------------"

echo "Testene er fullført."

# Disk I/O test
kjor_fio_test () {
  modus="$1" # write eller read
  echo "Starter $modus test ..."
  output=$(fio --name=seq_"$modus"_test --ioengine=sync --rw="$modus" --bs=1M --direct=1 --iodepth=2 --size=2G --numjobs=1 --runtime=60 --filename=/home/tropisk/Bachelor/vm/testfile --group_reporting)
  iops=$(echo "$output" | grep "IOPS=" | grep -oP "(?<=IOPS=)\d+")
  echo "Sekvensiell $modus: IOPS = $iops"
  echo "Fio $modus test fullført."
  echo "--------------------------------------------------"
}

# Kjører fio-tester for sekvensiell skriving og lesing
kjor_fio_test write
kjor_fio_test read

echo "Alle tester fullført."
