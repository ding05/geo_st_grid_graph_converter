import xarray as xr
import numpy as np

def input_grid(input_filepath: str) -> np.ndarray:
    """
    Read the input NC file that contains a spatiotemporal grid.
    :param input_filepath: the path to the input NC file
    :return: a NumPy array
    """
    # Open and read the input NC file.
    grid_dataset = xr.open_dataset(input_filepath, decode_times=False)
  
    # Convert the Xarray dataset into an Xarray array.
    grid_array = grid_dataset.to_array()
  
    # Convert the Xarray array into a NumPy array, by only selecting the 
    # first variable.
    grid = np.array(grid_array[0,:,:,:])
  
    return grid