import pandas as pd
import matplotlib.pyplot as plt

def parse_file(filepath):
    read_speed, write_speed = None, None
    with open(filepath, 'r') as file:
        for line in file:
            if "Lese:" in line:
                read_speed = float(line.split('(')[-1].split()[0])
            elif "Skrive:" in line:
                write_speed = float(line.split('(')[-1].split()[0])
    return read_speed, write_speed

# Filepaths to your data files
filepaths = ['VMResultater.txt', 'KubernetesResultater.txt', 'NativeResultater.txt', 'KonteinerResultater.txt']

custom_labels = ['Virtuell Maskin', 'Kubernetes', 'Vertsmaskin', 'Konteiner']

# Parse each file and collect data
data = {'Fil': [], 'Lese Hastighet (MiB/sec)': [], 'Skrive Hastighet (MiB/sec)': []}
for i, filepath in enumerate(filepaths, 1):
    read_speed, write_speed = parse_file(filepath)
    data['Fil'].append(custom_labels[i-1])  # Use custom labels here
    data['Lese Hastighet (MiB/sec)'].append(read_speed)
    data['Skrive Hastighet (MiB/sec)'].append(write_speed)

# Convert collected data into a pandas DataFrame
df = pd.DataFrame(data)

# Set the index to 'File' for better plotting
df.set_index('Fil', inplace=True)

# Plotting
ax = df.plot(kind='bar', figsize=(10, 6))
ax.set_axisbelow(True)
ax.set_ylabel('Hastighet (MiB/sec)')
ax.set_title('Minne Lese og Skrive hastighet')
plt.xticks(rotation=15)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.set_ylim(bottom=7000)

# Adding values above bars
for container in ax.containers:
    ax.bar_label(container, fmt='%.0f')

plt.savefig('minne_resultater.png')
plt.show()
