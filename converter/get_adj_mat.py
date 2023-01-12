import numpy as np
from scipy.stats.stats import pearsonr   

def get_adj_mat(node_feat_mat: np.ndarray, threshold: float) -> np.ndarray:
  """
  Get the adjacency matrix based on the correlations between the node 
  features.
  :param node_feat_mat: the node feature NumPy array
  :param threshold: the correlation threshold float
  """
  # Compute the correlations between node features and keep the ones with
  # their absolute values greater than the threshold, masked as tuples.
  adj_mask = []
  for i in range(len(node_feat_mat)):
    # Exclude self-connected nodes.
    for j in range(i + 1, len(node_feat_mat)):
      if abs(pearsonr(node_feat_mat[i], node_feat_mat[j])[0]) >= threshold:
        adj_mask.append((i, j))
        adj_mask.append((j, i))
  adj_mask = sorted(adj_mask)
  
  # Write the adjacency matrix in the form recognized by PyTorch Geometric.
  adj_mat = [[], []]
  for i in adj_mask:
    adj_mat[0].append(i[0])
    adj_mat[1].append(i[1])
  adj_mat = np.array(adj_mat)
  
  return adj_mat