import numpy as np
from numpy import save

def output(tesnor: np.ndarray, output_dirpath: str, filename: str) -> None:
    """
    Write the NumPy array into an output NPY file.
    :param tesnor: an NumPy array
    :param output_filepath: the path to the output TXT file
    :param filename: the name of the output NPY file
    """
    # Write the NumPy array into an output NPY file.
    save(str(output_dirpath) + '/' + filename + '.npy', tesnor)