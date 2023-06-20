import networkx as nx 
import matplotlib.pyplot as plt 
import numpy as np

class MindMap:
    def __init__(self, name):
        self.name = name
        self.graph = nx.MultiGraph()

    def add_idea(self):
        idea = input("Enter an idea name: ")
        self.graph.add_node(idea)
        self.add_connections(idea)

    def add_connections(self, idea):
        while True:
            connected_idea = input(f"Enter idea connected to {idea} q to quit")
            if not connected_idea or connected_idea == 'q':
                break
            self.graph.add_edge(idea, connected_idea)

    def get_ideas(self):
        '''
        return two ideas based on their
        position/structure within mindmap
        '''
        centrality_degree = nx.degree_centrality(self.graph)
        max_node = max(centrality_degree, key=centrality_degree.get)
        print(f'max_node {max_node} at {centrality_degree}')

                # Get the adjacency matrix
        adj_matrix = nx.adjacency_matrix(self.graph)

        # Convert the sparse matrix to a dense matrix
        adj_matrix_dense = adj_matrix.todense()
        adj_array = np.array(adj_matrix_dense)
        self.adj_array = adj_array

        print('adj_matrix:')
        print(adj_matrix_dense)
        eigenvalues = np.linalg.eigvals(adj_array)

        
    
        max_egien = np.argmax(eigenvalues)
        print(f'max_egien {max_egien} at {eigenvalues[max_egien]}')
        
    def draw_map(self):
        nx.draw(self.graph, with_labels=True)
        plt.show()

    def ideate(self):
        while True:
            print("\n1: Add an idea")
            print("2: View Map")
            print("3: Analyze Map")
            choice = input("What ch'ya wanna do? ")
            if choice == '1':
                self.add_idea()
            elif choice == '2':
                self.draw_map()
            elif choice == '3':
                self.get_ideas()
            else:
                break

if __name__ == "__main__":
    mm = MindMap("M3")
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
   
    mm.graph.add_edges_from(edges)
    mm.draw_map()
    mm.get_ideas()

    
