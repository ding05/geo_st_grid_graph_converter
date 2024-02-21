import numpy as np
#from scipy.stats.stats import pearsonr   
from scipy.stats import kendalltau

def get_adj_mat(node_feat_mat: np.ndarray, threshold: float, 
                is_directed_bool: bool, min_edges: int) -> np.ndarray:
    """
    Get the adjacency matrix based on the correlations between the node 
    features.
    :param node_feat_mat: the node feature NumPy array
    :param threshold: the correlation threshold float
    :param is_directed_bool: if the generated graph is directed boolean
    :param min_edges: the minimum number of edges for all nodes
    """
    # Compute the correlations between node features and keep the ones with
    # their absolute values greater than the threshold, masked as tuples.
    adj_mask = []
    
    # Two conditions: directed and undirected
    # To generate directed graphs
    if is_directed_bool:
        for i in range(len(node_feat_mat)):
            for j in range(len(node_feat_mat)):
                # Exclude self-connected nodes.
                if i != j:
                    #if abs(pearsonr(node_feat_mat[i][:-1], node_feat_mat[j][1:])[0]) >= threshold:
                    if abs(kendalltau(node_feat_mat[i][:-1], node_feat_mat[j][1:])[0]) >= threshold:
                        adj_mask.append((i, j))
                        print(f'Edge ({str(i)}, {str(j)}) was appeneded.')
    # To generate undirected graphs
    else:
        for i in range(len(node_feat_mat)):
            # Exclude self-connected nodes.
            for j in range(i + 1, len(node_feat_mat)):
                #if abs(pearsonr(node_feat_mat[i], node_feat_mat[j])[0]) >= threshold:
                if abs(kendalltau(node_feat_mat[i], node_feat_mat[j])[0]) >= threshold:
                    adj_mask.append((i, j))
                    adj_mask.append((j, i))
                    print(f'Edges ({str(i)}, {str(j)}) and ({str(j)}, {str(i)}) were', 
                          'appeneded.')
    adj_mask = sorted(adj_mask)
    
    # Add full connections for selected nodes if required, avoiding duplicates.
    # Convert the adjacency list to a set for efficient membership tests.
    adj_set = set(adj_mask)
    selected_nodes = [5612, 5104, 4610, 3260, 5242, 2004, 5263, 2801, 2058, 5005, 3124, 1734]
    for node in selected_nodes:
        for j in range(node_feat_mat.shape[0]):
            if node != j:
                # Check if the edge is already in the adjacency set
                if (node, j) not in adj_set:
                    adj_set.add((node, j))
                    print(f'Edge ({node}, {j}) was appended.')
                if not is_directed_bool and (j, node) not in adj_set:
                    adj_set.add((j, node))
                    print(f'Edge ({j}, {node}) was appended.')
    # Convert the adjacency set back to a list and sort it.
    adj_mask = sorted(adj_set)
    
    # Write the adjacency matrix in the form recognized by PyTorch Geometric.
    adj_mat = [[], []]
    for i in adj_mask:
        adj_mat[0].append(i[0])
        adj_mat[1].append(i[1])
    adj_mat = np.array(adj_mat)
    
    # Add edges to the nodes with fewer than the minimum number edges.
    if is_directed_bool:
        for i in range(node_feat_mat.shape[0]):
            # Check the number of current edges.
            pair_count = np.count_nonzero((adj_mat[0] == i) | (adj_mat[1] == i))
            while pair_count < min_edges:
                # Generate random node numbers for the target node to be connected to.
                new_num = np.random.randint(0, node_feat_mat.shape[0])
                while new_num == i:
                    new_num = np.random.randint(0, node_feat_mat.shape[0])
                new_pair = (i, new_num)
                if not np.any(np.all(np.transpose(adj_mat) == new_pair, axis=1)):
                    # Generate add the edge in one direction to the adjacency matrix. 
                    adj_mat = np.column_stack((adj_mat, new_pair))
                    print(f'Edges ({str(new_pair[0])}, {str(new_pair[1])}) were appeneded.')
                pair_count = np.count_nonzero((adj_mat[0] == i) | (adj_mat[1] == i))
    else:
        for i in range(node_feat_mat.shape[0]):
            # Check the number of current edges.
            pair_count = np.count_nonzero((adj_mat[0] == i) | (adj_mat[1] == i)) / 2
            while pair_count < min_edges:
                # Generate random node numbers for the target node to be connected to.
                new_num = np.random.randint(0, node_feat_mat.shape[0])
                while new_num == i:
                    new_num = np.random.randint(0, node_feat_mat.shape[0])
                new_pair = (i, new_num)
                if not np.any(np.all(np.transpose(adj_mat) == new_pair, axis=1)):
                    # Generate add the edges in two directions to the adjacency matrix. 
                    adj_mat = np.column_stack((adj_mat, new_pair))
                    adj_mat = np.column_stack((adj_mat, (new_pair[1], new_pair[0])))
                    print(f'Edges ({str(new_pair[0])}, {str(new_pair[1])}) and', 
                          f'({str(new_pair[1])}, {str(new_pair[0])}) were appeneded.')
                pair_count = np.count_nonzero((adj_mat[0] == i) | (adj_mat[1] == i)) / 2
    
    # Sort the adjacency matrix that has been stored in a NumPy array.
    sorted_indices = np.lexsort((adj_mat[1], adj_mat[0]))
    adj_mat = adj_mat[:, sorted_indices]
    
    return adj_mat