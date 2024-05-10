import re
import csv

def parse_and_export_to_csv(input_file, output_file):
    # Forberedelse av regex-mønstre for å identifisere de ulike testtypene
    cpu_pattern = re.compile(r"Test (\d+): Starter CPU-test med (\d+) tråd\(er\) og cpu-max-prime=(\d+) for \d+ sekunder.*?"
                             r"total number of events:\s+(\d+)", re.DOTALL)
    ram_pattern = re.compile(r"(Lese|Skrive): \d+\.\d+ MiB transferred \((\d+\.\d+) MiB/sec\)\nMinnetest i (lese|skrive)modus, Test (\d+) fullført")
    disk_pattern = re.compile(r"Starter (read|write) test, Test (\d+).*?\nSekvensiell (read|write): IOPS = (\d+)")

    data = {"CPU": [], "RAM": [], "Disk": []}

    # Les filen og ekstraher data basert på mønstre
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

        # CPU-tests
        for match in cpu_pattern.finditer(content):
            test_number, threads, cpu_max_prime, events = match.groups()
            data["CPU"].append((test_number, threads, cpu_max_prime, events))

        # RAM-tests
        for match in ram_pattern.finditer(content):
            mode, mib_sec, _, test_number = match.groups()
            data["RAM"].append((mode, test_number, mib_sec))

        # Disk-tests
        for match in disk_pattern.finditer(content):
            mode, test_number, _, iops = match.groups()
            data["Disk"].append((mode, test_number, iops))

    # Lagre data til CSV
    with open(output_file, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["Test Type", "Mode/Threads", "Test Number", "Events/IOPS/MiB/sec", "cpu-max-prime (Only CPU)"])
        for cpu in data["CPU"]:
            writer.writerow(["CPU", f"{cpu[1]} threads", cpu[0], cpu[3], cpu[2]])
        for ram in data["RAM"]:
            writer.writerow(["RAM", ram[0], ram[1], ram[2], ""])
        for disk in data["Disk"]:
            writer.writerow(["Disk", disk[0], disk[1], disk[2], ""])

if __name__ == "__main__":
    parse_and_export_to_csv('Herdet.txt', 'Herdet.csv')
