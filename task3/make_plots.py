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
            idx, val = int(row[0]), float(row[1])  # Convert to integer if necessary
            indices.append(idx)
            data.append(val)
        
        return indices, data

nodes = [0, 1, 2, 3]
colors = ['red', 'green', 'gold', 'blue']

# Report average time per iteration per node
for node in nodes:
    _, times = read_file(f'node_{node}_times.csv')
    print(f'\item Node {node} average iteration time: {sum(times) / len(times)} seconds')

# Report losses per node
for color, node in zip(colors, nodes):
    indices, losses = read_file(f'node_{node}_losses.csv')
    plt.plot(indices, losses, color=color, marker='o', label=f'Node {node}')

plt.title('Loss per Iteration')
plt.xlabel('Iteration #')
plt.ylabel('Loss')
plt.legend()
plt.savefig('losses.png', dpi=300)
