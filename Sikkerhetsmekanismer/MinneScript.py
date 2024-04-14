import pandas as pd
import matplotlib.pyplot as plt

def parse_file(filepath):
    """Ekstraherer lese- og skrivehastighet fra en gitt fil."""
    read_speed, write_speed = None, None
    with open(filepath, 'r') as file:
        for line in file:
            if "Lese:" in line:
                read_speed = float(line.split('(')[-1].split()[0])
            elif "Skrive:" in line:
                write_speed = float(line.split('(')[-1].split()[0])
    return read_speed, write_speed

# Filstier til dine datafiler
filepaths = [
    'Herdet.txt',
    'Auditing.txt',
    'RBAC.txt',
    'Standard.txt',
    'RoleSecurityAdmission.txt'
]

custom_labels = ['Herdet', 'Auditing', 'RBAC', 'Standard', 'Role Security Admission']

# Parse hver fil og samle data
data = {'Fil': [], 'Lese Hastighet (MiB/sec)': [], 'Skrive Hastighet (MiB/sec)': []}
for i, filepath in enumerate(filepaths):
    read_speed, write_speed = parse_file(filepath)
    data['Fil'].append(custom_labels[i])  # Bruk tilpassede etiketter her
    data['Lese Hastighet (MiB/sec)'].append(read_speed)
    data['Skrive Hastighet (MiB/sec)'].append(write_speed)

# Konverter innsamlede data til en pandas DataFrame
df = pd.DataFrame(data)

# Sett indeksen til 'Fil' for bedre plotting
df.set_index('Fil', inplace=True)

# Plotting
ax = df.plot(kind='bar', figsize=(10, 6))
ax.set_axisbelow(True)
ax.set_ylabel('Hastighet (MiB/sec)')
ax.set_title('Minne Lese og Skrive hastighet')
plt.xticks(rotation=15)
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.set_ylim(bottom=0)  # Juster denne basert på dine data

# Legger til verdier over stolpene
for container in ax.containers:
    ax.bar_label(container, fmt='%.0f')

plt.savefig('minne_resultater.png')
plt.show()
