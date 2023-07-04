import numpy as np
import pandas as pd

def drop_rows_with_nas(grid: np.ndarray, *args, **kwarg) -> np.ndarray:
    """
    Drop the rows with NAs in a NumPy array.
    :param input_filepath: a NumPy array possibly with NAs
    :return: a NumPy array
    """
    assert isinstance(grid, np.ndarray)
    grid_dropped = pd.DataFrame(grid).dropna(*args, **kwarg).values
    if grid.ndim == 1:
        grid_dropped = grid_dropped.flatten()
    
    return grid_dropped