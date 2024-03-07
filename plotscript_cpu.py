import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a Pandas DataFrame
df = pd.read_csv('./parset_cpu_resultater.csv')

# Convert Test Number, Threads, and cpu-max-prime to categorical for easier manipulation
df['Test Number'] = pd.Categorical(df['Test Number'])
df['Threads'] = pd.Categorical(df['Threads'])
df['cpu-max-prime'] = pd.Categorical(df['cpu-max-prime'])

# Get unique combinations of Threads and cpu-max-prime for plotting
combinations = df[['Threads', 'cpu-max-prime']].drop_duplicates()

# Plotting
for index, (threads, cpu_max_prime) in enumerate(combinations.values, start=1):
    # Filter the DataFrame for the current combination
    subset = df[(df['Threads'] == threads) & (df['cpu-max-prime'] == cpu_max_prime)]
    
    # Calculate the average of Total Number of Events
    avg_total_events = subset['Total Number of Events'].mean()
    
    # Plotting
    plt.figure(index)
    plt.plot(subset['Test Number'], subset['Total Number of Events'], label='Total Number of Events',  marker='o')
    plt.axhline(y=avg_total_events, color='black', linestyle='--', label=f'Gjennomsnitt: {avg_total_events:.2f}')
    
    plt.title(f'Tråder = {threads}, cpuMaxPrime = {cpu_max_prime}')
    plt.xlabel('Test Number')
    plt.ylabel('Total Number of Events')
    plt.legend()
    plt.grid(True)
    
    # Save the figure to a PNG file
    filename = f"graph_threads_{threads}_cpumax_{cpu_max_prime}.png"
    plt.savefig(filename, bbox_inches='tight')
    plt.close()  # Close the figure to free memory

print("Graphs have been saved as .png files.")

