# Geo Spatiotemporal Grid to Graph Converter

This program converts a geographic spatiotemporal grid in a NetCDF file into a graph in NumPy array files.

## Programming Language

Python 3.7.15

## Running converter

1. Make sure Python has been installed on your computer.
2. Navigate to [this](.) directory, which contains the README.md file.
3. Run the program as a module: `python -m converter -h`. This will print the help message.
4. Run the program as a module with real inputs: `python -m converter <input_filepath> <output_dirpath> <corr_threshold> <is_directed>`
   For input, i.e. `python -m converter data/era5_sst_011950_082022_globe.nc out 0.9 yes no`

### converter Usage:

```commandline
usage: python -m converter [-h] input_filepath output_dirpath

positional arguments:
  input_filepath     Input File Pathname
  output_dirpath     Output Directory Pathname
  corr_threshold     Node Feature Correlation Threshold
  is_directed        If Directed Graphs: `yes` or `no`
  get_coords         If Output Coordinates: `yes` or `no`

optional arguments:
  -h, --help  show this help message and exit
```