import pandas as pd
import matplotlib.pyplot as plt

def extract_iops(filename):
    """
    Extracts the IOPS values for write and read tests from a given file.
    """
    with open(filename, 'r') as file:
        content = file.read()
        write_iops = int(content.split('Sekvensiell write: IOPS = ')[1].split('\n')[0])
        read_iops = int(content.split('Sekvensiell read: IOPS = ')[1].split('\n')[0])
    return write_iops, read_iops

# Oppdaterte filstier
files = [
    'Herdet.txt',
    'Auditing.txt',
    'RBAC.txt',
    'Standard.txt',
    'RoleSecurityAdmission.txt'
]

# Initialiser en liste for å lagre data
data = []

# Hent data fra hver fil
for file in files:
    write_iops, read_iops = extract_iops(file)
    data.append({'Type': 'Skrive', 'IOPS': write_iops, 'File': file})
    data.append({'Type': 'Lese', 'IOPS': read_iops, 'File': file})

# Lag en DataFrame
df = pd.DataFrame(data)

# Definer en mapping av filnavn til mer lesbare navn
file_name_mapping = {
    'Herdet.txt': 'Herdet',
    'Auditing.txt': 'Auditing',
    'RBAC.txt': 'RBAC',
    'Standard.txt': 'Standard',
    'RoleSecurityAdmission.txt': 'Role Security Admission'
}

# Bruk mapping på DataFrame for å gjenspeile i plottet
df['File'] = df['File'].map(file_name_mapping)

# Plotting
fig, ax = plt.subplots(figsize=(10, 6))
bars = df.pivot(index='File', columns='Type', values='IOPS').plot(kind='bar', ax=ax)
ax.set_axisbelow(True)
plt.grid(True, which='major', linestyle='-', linewidth='0.5', color='grey', axis='both')
ax.set_title('Disk Ytelse')
ax.set_ylabel('IOPS')
ax.set_xlabel('File')
plt.xticks(rotation=15)
plt.legend(title='Test Type')
ax.set_ylim(bottom=250)  # Set the starting point of the y-axis to 250

# Adding values above bars
for container in bars.containers:
    ax.bar_label(container)

plt.tight_layout()
plt.savefig('disk_resultater.png')
