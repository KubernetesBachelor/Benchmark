import pandas as pd
import matplotlib.pyplot as plt

# Filnavn og etiketter for de fire datasettene
files = ['VM.csv', 'Konteiner.csv', 'Kubernetes.csv', 'Vertsmaskin.csv']
labels = ['VM', 'Konteiner', 'Kubernetes', 'Vertsmaskin']

# Plot funksjon for å tegne separate grafer for hver kombinasjon av tråder og cpu-max-prime for CPU
def plot_cpu_data():
    all_data = [pd.read_csv(file) for file in files]
    unique_combinations = set()
    for df in all_data:
        unique_combinations.update([(row['Mode/Threads'].split()[0], row['cpu-max-prime (Only CPU)'])
                                    for _, row in df[df['Test Type'] == 'CPU'].iterrows()])

    for threads, cpu_max_prime in sorted(unique_combinations, key=lambda x: (int(x[0]), int(x[1]))):
        plt.figure(figsize=(12, 8))
        for df, label in zip(all_data, labels):
            data = df[(df['Test Type'] == 'CPU') & (df['Mode/Threads'].str.startswith(threads)) &
                      (df['cpu-max-prime (Only CPU)'] == cpu_max_prime)]
            if not data.empty:
                avg_value = data['Events/IOPS/MiB/sec'].mean()
                plot = plt.plot(data['Test Number'], data['Events/IOPS/MiB/sec'], marker='o', label=label)
                plt.axhline(y=avg_value, color=plot[0].get_color(), linestyle='--', label=f'{label} Gj. snitt: {avg_value:.2f}')
        plt.title(f'CPU Ytelse: Tråd(er)={threads}, CPU Max Prime={cpu_max_prime}')
        plt.xlabel('Test Nummer')
        plt.ylabel('Antall Kalkulasjoner')
        plt.legend()
        plt.grid(True)
        plt.savefig(f'CPU_Threads_{threads}_CPU_Max_Prime_{cpu_max_prime}_Performance.png')

# Plot funksjon for å tegne grafer for RAM og Disk med gjennomsnitt
def plot_ram_disk_data(test_type, y_label, save_filename_prefix):
    all_data = [pd.read_csv(file) for file in files]
    modes = {'RAM': ['Lese', 'Skrive'], 'Disk': ['read', 'write']}
    for mode in modes[test_type]:
        plt.figure(figsize=(12, 8))
        for df, label in zip(all_data, labels):
            data = df[(df['Test Type'] == test_type) & (df['Mode/Threads'] == mode)]
            if not data.empty:
                avg_value = data['Events/IOPS/MiB/sec'].mean()
                plot = plt.plot(data['Test Number'], data['Events/IOPS/MiB/sec'], marker='o', label=f'{label} - {mode.capitalize()}')
                plt.axhline(y=avg_value, color=plot[0].get_color(), linestyle='--', label=f'{label} Gj. snitt: {avg_value:.2f}')
        plt.title(f'{test_type} Ytelsesmålinger: {mode.capitalize()}')
        plt.xlabel('Test Nummer')
        plt.ylabel(y_label)
        if plt.gca().has_data():
            plt.legend()
            plt.grid(True)
            plt.savefig(f'{save_filename_prefix}_{mode}_Performance.png')
        else:
            print(f"No data available to plot for {test_type} {mode.capitalize()}")

# Kall funksjonene for plotting
plot_cpu_data()
plot_ram_disk_data('RAM', 'MiB/sec', 'RAM')
plot_ram_disk_data('Disk', 'IOPS', 'Disk')
