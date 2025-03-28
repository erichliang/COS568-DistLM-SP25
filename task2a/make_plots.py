import matplotlib.pyplot as plt
import csv


# Read the CSV file
def read_file(filename):
with open(filename, mode='r') as file:
    indices = []
    data = []
    
    reader = csv.reader(file)
    
    # Skip the header row
    next(reader)

    # Read and print each row
    for row in reader:
        idx, val = int(row[0]), int(row[1])  # Convert to integer if necessary
        print(f"Index: {idx}, Value: {val}")
        indices.append(idx)
        data.append(val)
    
    return indices, data

# Report average time per iteration
breakpoint()
