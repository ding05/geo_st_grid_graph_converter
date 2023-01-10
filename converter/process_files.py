from converter.input import *
from converter.output import *

import numpy as np

def process_files(input_filepath: str, output_dirpath: str) -> None:
  """
  Read the NC file that contains a spatiotemporal grid, and output the 
  converted graph in NPY files.
  :param input_filepath: the path to the input NC file
  :param output_dirpath: the path to the output directory
  """
  # Generate and save the vertex feature tensor.
  grid = input_grid(input_filepath)
  grid_transposed = grid.transpose(1,2,0)
  grid_flattened = grid_transposed.reshape(grid_transposed.shape[0] * 
                                           grid_transposed.shape[1], 
                                           grid_transposed.shape[2])
  vertex_feats = grid_flattened
  output(vertex_feats, output_dirpath, "vertex_feats")