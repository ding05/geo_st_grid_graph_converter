import numpy as np
from numpy import save

def output(tesnor: np.ndarray, output_dirpath: str, filename: str) -> None:
  """
  Write the NumPy array into an output NPY file.
  :param postfix_array_list: a list of strings
  :param output_filepath: the path to the output TXT file
  """
  # Write the NumPy array into an output NPY file.\
  save(str(output_dirpath) + '/' + filename + '.npy', tesnor)