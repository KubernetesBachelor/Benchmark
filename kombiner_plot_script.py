import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files into Pandas DataFrames
df1 = pd.read_csv('./parset_cpu_resultater_Konteiner.csv')
df2 = pd.read_csv('./parset_cpu_resultater_VM.csv')

# Determine all combinations of threads and cpu-max-prime in the datasets
combinations = pd.concat([df1[['Threads', 'cpu-max-prime']], df2[['Threads', 'cpu-max-prime']]]).drop_duplicates()

# Create plots for each combination
for _, row in combinations.iterrows():
    threads = row['Threads']
    cpu_max_prime = row['cpu-max-prime']
    
    # Filter data for the current combination
    data1 = df1[(df1['Threads'] == threads) & (df1['cpu-max-prime'] == cpu_max_prime)]
    data2 = df2[(df2['Threads'] == threads) & (df2['cpu-max-prime'] == cpu_max_prime)]
    
    # Calculate and plot averages
    avg1 = data1['Total Number of Events'].mean()
    avg2 = data2['Total Number of Events'].mean()
    
    # Find the highest y-value across both datasets
    max_y_value = max(data1['Total Number of Events'].max(), data2['Total Number of Events'].max())
    
    # Calculate 2/3 of the maximum y-value
    min_y_value = 2/3 * max_y_value

    # Create a new figure for the plot
    plt.figure(figsize=(10, 6))
    
    # Plot data from both files
    plt.plot(data1['Test Number'], data1['Total Number of Events'], label='Konteiner', marker='o')
    plt.plot(data2['Test Number'], data2['Total Number of Events'], label='VM', marker='o')
    
    plt.axhline(y=avg1, color='blue', linestyle='--', label=f'Konteiner Gjennomsnitt: {avg1:.2f}')
    plt.axhline(y=avg2, color='orange', linestyle='--', label=f'VM Gjennomsnitt: {avg2:.2f}')
    
    # Set y-axis to start from 2/3 of the highest y-value
    plt.ylim(bottom=min_y_value, top=max_y_value*1.05)  # Add a little buffer to the top for visibility
    
    # Formatting the plot
    plt.title(f'Tråder = {threads}, cpuMaxPrime = {cpu_max_prime}')
    plt.xlabel('Test Number')
    plt.ylabel('Total Number of Events')
    plt.legend()
    plt.grid(True)
    
    # Save the figure
    filename = f'combined_graph_threads_{threads}_cpuMaxPrime_{cpu_max_prime}.png'
    plt.savefig(filename, bbox_inches='tight')
    plt.close()  # Close the plot to free up memory

print("All combined graphs have been saved as .png files.")
