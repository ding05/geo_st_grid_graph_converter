import xarray as xr
import numpy as np

def get_coord_mat(input_filepath: str) -> np.ndarray:
    """
    Read the input NC file that contains a spatiotemporal grid and return
    a two-column (lats and lons) coordinate matrix
    :param input_filepath: the path to the input NC file
    :return: a NumPy array
    """
    # Open and read the input NC file.
    grid_dataset = xr.open_dataset(input_filepath, decode_times=False)
  
    # Get the latitute grid and the longitute grid.
    lat_grid, lon_grid = np.meshgrid(grid_dataset.lat, grid_dataset.lon)
    lat_grid, lon_grid = np.transpose(lat_grid), np.transpose(lon_grid) 
    
    # Flatten the two grids.
    lat_grid_flattened = lat_grid.reshape(lat_grid.shape[0] * 
                                          lat_grid.shape[1]) 
    lon_grid_flattened = lon_grid.reshape(lon_grid.shape[0] * 
                                          lon_grid.shape[1])
    
    # Create a new numpy array with latitutes as the first column and 
    # longitutes as the second column.
    coordinate_grid_flattened = np.column_stack((lat_grid_flattened, 
                                                 lon_grid_flattened))
    
    return coordinate_grid_flattened