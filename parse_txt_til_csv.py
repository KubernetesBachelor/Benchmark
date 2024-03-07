import re
import csv

def parse_text_to_csv(input_file_path, output_csv_path):
    # Regular expressions to match relevant lines
    test_start_re = re.compile(r"Test (\d+): Starter CPU-test med (\d+) tråd\(er\) og cpu-max-prime=(\d+) for 30 sekunder...")
    total_time_re = re.compile(r"total time:\s+(\d+\.\d+)s")
    total_events_re = re.compile(r"total number of events:\s+(\d+)")
    
    # Open the input file and a new output CSV file
    with open(input_file_path, 'r') as infile, open(output_csv_path, 'w', newline='') as outfile:
        csv_writer = csv.writer(outfile)
        # Write the header row in the CSV file
        csv_writer.writerow(["Test Number", "Threads", "cpu-max-prime", "Total Time (s)", "Total Number of Events"])
        
        # Variables to track the current test's data
        current_test_data = None
        
        for line in infile:
            # Check if the line indicates the start of a test
            start_match = test_start_re.match(line)
            if start_match:
                # If we have data from a previous test, write it before starting a new one
                if current_test_data:
                    csv_writer.writerow(current_test_data)
                    current_test_data = None  # Reset for the next test
                
                # Initialize current test data with the new test's details
                test_number, threads, cpu_max_prime = start_match.groups()
                current_test_data = [test_number, threads, cpu_max_prime, None, None]  # Placeholder for time and events

            # For matching total time and total number of events
            if current_test_data:  # Ensure we've started a new test
                time_match = total_time_re.search(line)
                events_match = total_events_re.search(line)
                if time_match:
                    current_test_data[3] = time_match.group(1)
                if events_match:
                    current_test_data[4] = events_match.group(1)

        # After reading all lines, make sure to write the last test's data if it exists
        if current_test_data and None not in current_test_data:  # Check if the last test's data is complete
            csv_writer.writerow(current_test_data)

# Example usage
input_file_path = 'path_to_your_input_file.txt'
output_csv_path = 'path_to_your_output_file.csv'
parse_text_to_csv(input_file_path, output_csv_path)
