from converter.input import *
from converter.get_coord_mat import *
from converter.get_adj_mat import *
from converter.drop_nodes import *
from converter.output import *

import numpy as np

def process_files(input_filepath: str, output_dirpath: str, 
                  corr_threshold: str, is_directed: str,
                  get_coords: str, min_edges: str, max_edges: str) -> None:
    """
    Read the NC file that contains a spatiotemporal grid, and output the 
    converted graph in NPY files.
    :param input_filepath: the path to the input NC file
    :param output_dirpath: the path to the output directory
    :param corr_threshold: the corrleation threshold to mask adjacencies
    :param is_directed: if the generated graph is directed
    :param get_coords: if the node coordinates are output
    :param min_edges: the minimum number of edges for all nodes
    :param max_edges: the minimum number of edges for all nodes
    """
    # Generate and save the node feature tensor.
    grid = input_grid(input_filepath)
    
    # Get the coordinate tensor.
    coordinate_grid = get_coord_mat(input_filepath)
    grid_transposed = grid.transpose(1,2,0)
    grid_flattened = grid_transposed.reshape(grid_transposed.shape[0] * 
                                             grid_transposed.shape[1], 
                                             grid_transposed.shape[2])
                                             
    # Remove nodes with NAs.
    node_feats = drop_rows_with_nas(grid_flattened)
    output(node_feats, output_dirpath, 'node_feats')
    
    # Temporary: Test the program with a smaller node feature matrix.
    # Comment the line below when normally running the program.
    #node_feats = node_feats[:200]
    
    # Output the coordinate tensor (slow).
    if str(get_coords) == 'yes':
        # Also remove the corresponding nodes in the coorindate tensor.
        land_indices = np.setdiff1d(np.arange(grid_flattened.shape[0]), np.where(
                       (grid_flattened[:, np.newaxis] == node_feats).all(-1))[0])
        coordinates_ocean = np.delete(coordinate_grid, land_indices, axis=0)
        output(coordinates_ocean, output_dirpath, 'coords')
  
    # Convert the string into the numerical.
    corr_threshold = float(str(corr_threshold))
    min_edges = int(str(min_edges))
    max_edges = int(str(max_edges))
    
    # Convert the string into the boolean.
    is_directed_bool = True if str(is_directed) is 'yes' else False
    is_directed_printed = '_directed' if is_directed_bool else ''
    adj_mat = get_adj_mat(node_feats, corr_threshold, is_directed_bool, min_edges, max_edges)
    output(adj_mat, output_dirpath, 'adj_mat' + '_' + str(corr_threshold) + 
           '_' + str(min_edges) + '_' + str(max_edges) + is_directed_printed)