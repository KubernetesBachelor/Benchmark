import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def plot_tests(csv_files, file_labels, test_type, identifiers, value_column):
    output_dir = f'{test_type.lower()}_output_graphs'
    os.makedirs(output_dir, exist_ok=True)
    results = {}

    for csv_file, label in zip(csv_files, file_labels):
        data = pd.read_csv(csv_file)
        specific_data = data[data['Test Type'] == test_type]

        if isinstance(identifiers, list):
            group_columns = identifiers
        else:
            group_columns = [identifiers]

        for key, group_data in specific_data.groupby(group_columns):
            if isinstance(key, tuple):
                key_str = '_'.join(map(str, key))
            else:
                key_str = str(key)

            if key not in results:
                results[key] = []

            mean = group_data[value_column].mean()
            std = group_data[value_column].std()
            results[key].append((mean, std, label))

    for key, stats in results.items():
        if isinstance(key, tuple):
            key_str = '_'.join(map(str, key))
        else:
            key_str = str(key)

        fig, ax = plt.subplots()
        means = [stat[0] for stat in stats]
        stds = [stat[1] for stat in stats]
        labels = [stat[2] for stat in stats]

        bar_positions = np.arange(len(means))
        bars = ax.bar(bar_positions, means, yerr=stds, capsize=5, color='skyblue', alpha=0.7)

        # Justering av y-aksen basert på verdiene
        upper_limit = max([m + s for m, s in zip(means, stds)]) * 1.2
        ax.set_ylim(0, upper_limit)

        ax.set_xticks(bar_positions)
        ax.set_xticklabels(labels)

        if test_type == 'CPU':
            ylabel = 'Antall Hendelser'
            title = f'CPU Ytelse - {key[0]}, CPU max prime {key[1]}'
        elif test_type == 'Disk':
            ylabel = 'IOPS'
            title = f'Disk Ytelse - {key_str}'
        elif test_type == 'RAM':
            ylabel = 'MiB/sec'
            title = f'Minne Ytelse - {key_str}'

        ax.set_title(title)
        ax.set_ylabel(ylabel)

        # Visning av gjennomsnittsverdier i en boks
        text_str = '\n'.join([f'{label}: {mean:.2f}' for mean, _, label in zip(means, stds, labels)])
        ax.text(0.02, 0.98, text_str, transform=ax.transAxes, fontsize=10,
                verticalalignment='top', horizontalalignment='left', bbox=dict(boxstyle="round,pad=0.3", facecolor='lightblue', edgecolor='black', alpha=0.5))

        # Lagre plottet
        plt.savefig(f'{output_dir}/{test_type}_{key_str.replace(" ", "_")}.png')
        plt.close()

# Eksempel på bruk
csv_files = ['VM.csv', 'Konteiner.csv', 'Kubernetes.csv', 'Vertsmaskin.csv']
file_labels = ['VM', 'Konteiner', 'Kubernetes', 'Vertsmaskin']

plot_tests(csv_files, file_labels, 'CPU', ['Mode/Threads', 'cpu-max-prime (Only CPU)'], 'Events/IOPS/MiB/sec')
plot_tests(csv_files, file_labels, 'RAM', 'Mode/Threads', 'Events/IOPS/MiB/sec')
plot_tests(csv_files, file_labels, 'Disk', 'Mode/Threads', 'Events/IOPS/MiB/sec')
