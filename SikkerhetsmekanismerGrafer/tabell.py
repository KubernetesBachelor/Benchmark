import pandas as pd
import numpy as np
import os

def calculate_percentage_differences(csv_files, file_labels, test_types, identifiers_dict, value_column):
    output_dir = 'percentage_differences'
    os.makedirs(output_dir, exist_ok=True)
    all_data = []

    for test_type in test_types:
        results = {}
        base_means = {}
        identifiers = identifiers_dict[test_type]  # Velg riktig identifiers basert på testtypen

        for csv_file, label in zip(csv_files, file_labels):
            data = pd.read_csv(csv_file)
            specific_data = data[data['Test Type'] == test_type]

            group_columns = identifiers if isinstance(identifiers, list) else [identifiers]

            for key, group_data in specific_data.groupby(group_columns):
                key_str = '_'.join(map(str, key)) if isinstance(key, tuple) else str(key)

                if key not in results:
                    results[key] = {}

                mean = group_data[value_column].mean()
                results[key][label] = mean

                if label == 'Standard':
                    base_means[key] = mean

        # Beregne prosentforskjeller
        for key, labels_means in results.items():
            base_mean = base_means[key]
            for label, mean in labels_means.items():
                percentage_diff = ((mean / base_mean * 100) - 100) if base_mean != 0 else float('inf')
                all_data.append({
                    'Test Type': test_type,
                    'Configuration': key,
                    'Label': label,
                    'Percentage Difference': percentage_diff
                })

    # Opprett en DataFrame fra samlet data
    df = pd.DataFrame(all_data)
    df.to_csv(f'{output_dir}/all_percentage_differences.csv', index=False)
    print(f'Samlet tabell lagret: {output_dir}/all_percentage_differences1.csv')

# Bruk av funksjonen
csv_files = [
    'Standard.csv',
    'PSA.csv',
    'RBAC.csv',
    'Auditing.csv',
    'Herdet.csv'
]
file_labels = ['Standard', 'PSA', 'RBAC', 'Auditing', 'Herdet']
test_types = ['CPU', 'RAM', 'Disk']

identifiers_dict = {
    'CPU': ['Mode/Threads', 'cpu-max-prime (Only CPU)'],
    'RAM': 'Mode/Threads',  # Anta at RAM og Disk har samme identifikator
    'Disk': 'Mode/Threads'
}

calculate_percentage_differences(csv_files, file_labels, test_types, identifiers_dict, 'Events/IOPS/MiB/sec')
