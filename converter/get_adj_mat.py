import numpy as np
#from scipy.stats.stats import pearsonr   
from scipy.stats import kendalltau
from collections import defaultdict

def get_adj_mat(node_feat_mat: np.ndarray, threshold: float, 
                is_directed_bool: bool, min_edges: int, max_edges: int) -> np.ndarray:
    """
    Get the adjacency matrix based on the correlations between the node 
    features.
    :param node_feat_mat: the node feature NumPy array
    :param threshold: the correlation threshold float
    :param is_directed_bool: if the generated graph is directed boolean
    :param min_edges: the minimum number of edges for all nodes
    """
    n = len(node_feat_mat)
    
    # A dictionary that will store edges as keys and their correlations as values
    correlations = defaultdict(float)

    if is_directed_bool:
        for i in range(n):
            for j in range(n):
                if i != j:
                    correlation = kendalltau(node_feat_mat[i], node_feat_mat[j])[0]
                    correlations[(i, j)] = correlation
                    print(f'Edges ({str(i)}, {str(j)}) was appeneded.')
    else:
        for i in range(n):
            for j in range(i + 1, n):
                correlation = kendalltau(node_feat_mat[i], node_feat_mat[j])[0]
                if abs(correlation) >= threshold:
                    correlations[(i, j)] = correlation
                    correlations[(j, i)] = correlation
                    print(f'Edges ({str(i)}, {str(j)}) and', 
                          f'({str(j)}, {str(i)}) were appeneded.')
    
    if max_edges > 0:
        # Sort correlations by absolute value in descending order.
        sorted_correlations = sorted(correlations.items(), key=lambda x: -abs(x[1]))
        # Get the top edges with the highest correlations.
        top_edges = [edge[0] for edge in sorted_correlations[:max_edges]]
        
    else:
        # Start with an empty adjacency matrix.
        adj_mat = [[], []]
        for edge, _ in correlations.items():
            if is_directed_bool or edge[0] < edge[1]:
                adj_mat[0].append(edge[0])
                adj_mat[1].append(edge[1])
                print(f'Edge ({edge[0]}, {edge[1]}) was appended.')
                
        # Handle the directed graph case.
        if is_directed_bool:
            for i in range(n):
                pair_count = np.count_nonzero((adj_mat[0] == i) | (adj_mat[1] == i))
                while pair_count < min_edges:
                    new_num = np.random.randint(n)
                    while new_num == i:
                        new_num = np.random.randint(n)
                    new_pair = (i, new_num)
                    if new_pair not in correlations:
                        adj_mat[0].append(new_pair[0])
                        adj_mat[1].append(new_pair[1])
                        print(f'Edge ({new_pair[0]}, {new_pair[1]}) was appended.')
                        pair_count += 1
                        
        # Handle the undirected graph case.
        else:
            for i in range(n):
                pair_count = np.count_nonzero((adj_mat[0] == i) | (adj_mat[1] == i)) / 2
                while pair_count < min_edges:
                    new_num = np.random.randint(n)
                    while new_num == i:
                        new_num = np.random.randint(n)
                    new_pair = (i, new_num)
                    if new_pair not in correlations:
                        adj_mat[0].append(new_pair[0])
                        adj_mat[1].append(new_pair[1])
                        adj_mat[0].append(new_pair[1])
                        adj_mat[1].append(new_pair[0])
                        print(f'Edges ({new_pair[0]}, {new_pair[1]}) and',
                              f'({new_pair[1]}, {new_pair[0]}) were appended.')
                        pair_count += 1
                        
        top_edges = list(zip(adj_mat[0], adj_mat[1]))

    # Convert the list of edges to an adjacency matrix format.
    adj_mat = np.array(top_edges).T
    
    return adj_mat