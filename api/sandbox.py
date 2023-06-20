import numpy as np

import numpy as np
edges = [
    (1,2), (1,4), (1,7), (1,8), (1,10),
    (2,6), (2,7), (2,9),(2,11),(2,12),(2,13),(2,18),(2,19),(2,20),
    (4,5), (4,6), (4,10), (4,17),
    (6,7), (6,8),
    (7,9),
    (8,9),(8,10),(8,11),(8,19),
    (9,11), (9,12), (9,13),(9,18),(9,19),(9,20),
    (10,11),
    (11,12), (11,13), (11,14), (11,17), (11,18), (11,19),
    (12,16), (12,17), (12,19),
    (13,14), (13,17), (13,18), (13,19), (13,20),
    (18,19),(18,20),
    (19,20)
]

# Find the maximum node number to determine the size of the adjacency matrix

# Initialize the adjacency matrix
adj_matrix = np.zeros((20, 20))

# Fill in the adjacency matrix based on the edges
for edge in edges:
    node1, node2 = edge
    adj_matrix[node1-1, node2-1] = 1
    adj_matrix[node2-1, node1-1] = 1

# Calculate the eigenvalues of the adjacency matrix
eigenvalues = np.linalg.eigvals(adj_matrix)

# Find the row index with the highest eigenvalue
max_eigenvalue_row = np.argmax(eigenvalues)
np.arg

print("Adjacency Matrix:")
print(adj_matrix)
print("Eigenvalues:", eigenvalues)
print(f'Row with highest ev {max_eigenvalue_row}')

