import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV files into Pandas DataFrames
df1 = pd.read_csv('./parset_cpu_resultater_Konteiner.csv')
df2 = pd.read_csv('./parset_cpu_resultater_VM.csv')
df3 = pd.read_csv('./parset_cpu_resultater_Native.csv')  # Assuming this is correct from previous context
df4 = pd.read_csv('./parset_cpu_resultater_Kubernetes.csv')  # The new fourth file

# Determine all combinations of threads and cpu-max-prime in the datasets
combinations = pd.concat([df1[['Threads', 'cpu-max-prime']], df2[['Threads', 'cpu-max-prime']], 
                          df3[['Threads', 'cpu-max-prime']], df4[['Threads', 'cpu-max-prime']]]).drop_duplicates()

# Create plots for each combination
for _, row in combinations.iterrows():
    threads = row['Threads']
    cpu_max_prime = row['cpu-max-prime']
    
    # Filter data for the current combination from all four datasets
    data1 = df1[(df1['Threads'] == threads) & (df1['cpu-max-prime'] == cpu_max_prime)]
    data2 = df2[(df2['Threads'] == threads) & (df2['cpu-max-prime'] == cpu_max_prime)]
    data3 = df3[(df3['Threads'] == threads) & (df3['cpu-max-prime'] == cpu_max_prime)]
    data4 = df4[(df4['Threads'] == threads) & (df4['cpu-max-prime'] == cpu_max_prime)]
    
    # Calculate and plot averages for all datasets
    avg1 = data1['Total Number of Events'].mean()
    avg2 = data2['Total Number of Events'].mean()
    avg3 = data3['Total Number of Events'].mean()
    avg4 = data4['Total Number of Events'].mean()
    
    # Find the highest y-value across all datasets for consistent y-axis limits
    max_y_value = max(data1['Total Number of Events'].max(), data2['Total Number of Events'].max(),
                      data3['Total Number of Events'].max(), data4['Total Number of Events'].max())
    
    # Adjust min_y_value based on the number of threads
    if threads == 1:
        # Calculate 2/3 of the maximum y-value for minimum y-axis value when threads = 1
        min_y_value = 2/3 * max_y_value
    elif threads == 2:
        # Calculate 1/3 of the maximum y-value for minimum y-axis value when threads = 2
        min_y_value = 2/3 * max_y_value
    else:
        # Default case, can adjust as needed or handle other thread values
        min_y_value = 1/2 * max_y_value  # Or any other default behavior you want

    # Set y-axis to start from calculated min_y_value and a little above max_y_value for visibility
    plt.ylim(bottom=min_y_value, top=max_y_value*1.05)


    # Create a new figure for the plot
    plt.figure(figsize=(10, 6))
    
    # Plot data from all four files
    plt.plot(data1['Test Number'], data1['Total Number of Events'], label='Konteiner', marker='o')
    plt.plot(data2['Test Number'], data2['Total Number of Events'], label='Virtuell Maskin', marker='o')
    plt.plot(data3['Test Number'], data3['Total Number of Events'], label='Vertsmaskin', marker='x')
    plt.plot(data4['Test Number'], data4['Total Number of Events'], label='Kubernetes', marker='^')  # New data plotted here
    
    plt.axhline(y=avg1, color='blue', linestyle='--', label=f'Konteiner Gjennomsnitt: {avg1:.2f}')
    plt.axhline(y=avg2, color='orange', linestyle='--', label=f'VM Gjennomsnitt: {avg2:.2f}')
    plt.axhline(y=avg3, color='green', linestyle='--', label=f'Vertsmaskin Gjennomsnitt: {avg3:.2f}')
    plt.axhline(y=avg4, color='red', linestyle='--', label=f'Kubernetes Gjennomsnitt: {avg4:.2f}')  # New average line
    
    # Set y-axis to start from 2/3 of the highest y-value
    plt.ylim(bottom=min_y_value, top=max_y_value*1.05)  # Add a little buffer to the top for visibility
    
    # Formatting the plot
    plt.title(f'Threads = {threads}, cpuMaxPrime = {cpu_max_prime}')
    plt.xlabel('Test Number')
    plt.ylabel('Total Number of Events')
    plt.legend()
    plt.grid(True)
    
    # Save the figure
    filename = f'combined_graph_threads_{threads}_cpuMaxPrime_{cpu_max_prime}.png'
    plt.savefig(filename, bbox_inches='tight')
