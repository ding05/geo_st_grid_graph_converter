import numpy as np
#from scipy.stats.stats import pearsonr   
from scipy.stats import kendalltau

def get_adj_mat(node_feat_mat: np.ndarray, fixed_edges: int, 
                is_directed_bool: bool, is_full_to_selected_nodes: bool) -> np.ndarray:
    """
    Get the adjacency matrix based on the correlations between the node 
    features.
    :param node_feat_mat: the node feature NumPy array
    :param fixed_edges: the fixed number of edges for all nodes
    :param is_directed_bool: if the generated graph is directed
    :param is_full_to_selected_nodes: if all edges are added to the selected nodes
    """
    # Compute the correlations between node features and keep the fixed_edges ones. 
    # with largest absolute values, masked as tuples.
    # Time complexity: calculate correlations: O(n^2 * m * log(m)), sort: O(n^2 log(n)),
    # where n is the number of nodes and m is the number of features.
    # Space complexity: O(n^2)
    selected_nodes = [5612, 5104, 4610, 3260, 5242, 2004, 5263, 2801, 2058, 5005, 3124, 1734]
    num_nodes = len(node_feat_mat)
    adj_set = set()  # Use a set to prevent duplicates, instead of a list.

    for i in range(num_nodes):
        correlations = []

        # Calculate correlations for node i.
        for j in range(num_nodes):
            if i != j:
                correlation = kendalltau(node_feat_mat[i], node_feat_mat[j])[0]
                correlations.append((j, correlation))

        # Sort by the absolute correlation value and keep only up to fixed_edges.
        correlations = sorted(correlations, key=lambda x: -abs(x[1]))[:fixed_edges]

        for j, _ in correlations:
            edge = (i, j) if is_directed_bool else tuple(sorted((i, j))) # Sort if undirected.
            if edge not in adj_set: # Check if the edge is already added.
                adj_set.add(edge)
                print(f'Edge {edge} was appended.')
                if not is_directed_bool:
                    adj_set.add((edge[1], edge[0])) # Add the reverse edge if undirected.

    # Add full connections for selected nodes if required.
    if is_full_to_selected_nodes:
        for node in selected_nodes:
            for j in range(num_nodes):
                if node != j:
                    edge = (node, j) if is_directed_bool else tuple(sorted((node, j)))
                    if edge not in adj_set:  # Check if the edge is already added.
                        adj_set.add(edge)
                        print(f'Edge {edge} was appended.')
                        if not is_directed_bool:
                            adj_set.add((edge[1], edge[0])) # Add the reverse edge if undirected.

    # Convert set to a sorted list
    adj_list = sorted(list(adj_set), key=lambda x: (x[0], x[1]))
    adj_mat = np.array(adj_list).T  # Transpose to get 2 rows: source nodes and target nodes.
    
    return adj_mat