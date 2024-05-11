#!/bin/bash

resultatfil="resultater.txt" # Definerer navnet på resultatfilen
echo "Starter stresstesting av konteineren ..."

# Sørger for at resultatfilen er tom før vi starter
echo "" > "$resultatfil"

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
for i in {1..10}; do
  echo "Starter minnetest i lesemodus, Test $i..."
  echo "Starter minnetest i lesemodus, Test $i..." >> "$resultatfil"
  output=$(sysbench memory --memory-block-size=128M --memory-total-size=1G --memory-oper=read --threads=1 run)
  filtered_output=$(echo "$output" | grep -oP "\d+(\.\d+)? MiB transferred \(\d+(\.\d+)? MiB/sec\)" | uniq)
  echo "Lese: $filtered_output"
  echo "Lese: $filtered_output" >> "$resultatfil"
  echo "Minnetest i lesemodus, Test $i fullført."
  echo "Minnetest i lesemodus, Test $i fullført." >> "$resultatfil"
  echo "--------------------------------------------------"
  echo "--------------------------------------------------" >> "$resultatfil"
done

# Minnetest 2 - Skrive
for i in {1..10}; do
  echo "Starter minnetest i skrivemodus, Test $i..."
  echo "Starter minnetest i skrivemodus, Test $i..." >> "$resultatfil"
  output=$(sysbench memory --memory-block-size=128M --memory-total-size=1G --memory-oper=write --threads=1 run)
  filtered_output=$(echo "$output" | grep -oP "\d+(\.\d+)? MiB transferred \(\d+(\.\d+)? MiB/sec\)" | uniq)
  echo "Skrive: $filtered_output"
  echo "Skrive: $filtered_output" >> "$resultatfil"
  echo "Minnetest i skrivemodus, Test $i fullført."
  echo "Minnetest i skrivemodus, Test $i fullført." >> "$resultatfil"
  echo "--------------------------------------------------"
  echo "--------------------------------------------------" >> "$resultatfil"
done

# Disk I/O test
kjor_fio_test () {
  modus="$1" # write eller read
  for i in {1..10}; do
    echo "Starter $modus test, Test $i..."
    echo "Starter $modus test, Test $i..." >> "$resultatfil"
    output=$(fio --name=seq_"$modus"_test --ioengine=sync --rw="$modus" --bs=1M --direct=1 --iodepth=1 --size=2G --numjobs=1 --runtime=60 --filename=/home/tropisk/Bachelor/vm/testfile --group_reporting)
    echo "$output" >> "fio_full_output_$modus.txt"
    iops=$(echo "$output" | grep "IOPS=" | grep -oP "(?<=IOPS=)\d+")
    echo "Sekvensiell $modus: IOPS = $iops"
    echo "Sekvensiell $modus: IOPS = $iops" >> "$resultatfil"
    echo "Fio $modus test, Test $i fullført."
    echo "Fio $modus test, Test $i fullført." >> "$resultatfil"
    echo "--------------------------------------------------"
    echo "--------------------------------------------------" >> "$resultatfil"
  done
}

# Kjører fio-tester for sekvensiell skriving og lesing
kjor_fio_test write
kjor_fio_test read

echo "Testene er fullført og resultatene er lagret i $resultatfil."
echo "Alle tester fullført."
