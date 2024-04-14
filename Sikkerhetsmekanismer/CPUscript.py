import pandas as pd
import matplotlib.pyplot as plt

# Last inn CSV-filene i Pandas DataFrames
df1 = pd.read_csv('./Herdet.csv')
df2 = pd.read_csv('./Auditing.csv')
df3 = pd.read_csv('./RBAC.csv')
df4 = pd.read_csv('./Standard.csv')
df5 = pd.read_csv('./RoleSecurityAdmission.csv')

# Bestem alle kombinasjoner av tråder og cpu-max-prime i datasettene
combinations = pd.concat([
    df1[['Threads', 'cpu-max-prime']],
    df2[['Threads', 'cpu-max-prime']],
    df3[['Threads', 'cpu-max-prime']],
    df4[['Threads', 'cpu-max-prime']],
    df5[['Threads', 'cpu-max-prime']]
]).drop_duplicates().reset_index(drop=True)

# Opprett plot for hver kombinasjon
for _, row in combinations.iterrows():
    threads = row['Threads']
    cpu_max_prime = row['cpu-max-prime']

    # Opprett en ny figur for plottet
    plt.figure(figsize=(10, 6))

    for df, label, marker, color in zip(
        [df1, df2, df3, df4, df5],
        ['Herdet', 'Auditing', 'RBAC', 'Standard', 'Role Security Admission'],
        ['o', 'o', 'o', 'o', 'o'],
        ['blue', 'orange', 'green', 'red', 'purple']
    ):
        # Filtrer data for den aktuelle kombinasjonen fra datasettet
        data = df[(df['Threads'] == threads) & (df['cpu-max-prime'] == cpu_max_prime)]

        if not data.empty:
            plt.plot(data['Test Number'], data['Total Number of Events'], label=label, marker=marker, color=color)

            # Beregn gjennomsnittet for datasettet
            avg = data['Total Number of Events'].mean()
            plt.axhline(y=avg, color=color, linestyle='--', label=f'{label} Gjennomsnitt: {avg:.2f}')

    # Formatering av plottet
    plt.title(f'Tråder = {threads}, cpuMaxPrime = {cpu_max_prime}')
    plt.xlabel('Testnummer')
    plt.ylabel('Totalt antall hendelser')
    plt.legend()
    plt.grid(True)

    # Lagre figuren
    filename = f'combined_graph_threads_{threads}_cpuMaxPrime_{cpu_max_prime}.png'
    plt.savefig(filename, bbox_inches='tight')
    plt.close()  # Lukk figuren for å frigjøre minne
