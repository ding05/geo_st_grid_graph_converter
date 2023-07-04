# Geo-Spatiotemporal Grid to Graph Converter

This program converts a geographic spatiotemporal grid in a NetCDF file into a graph in NumPy array files.

## Programming Language

Python 3.7.15

## Running converter

1. Make sure Python has been installed on your computer.
2. Navigate to [this](.) directory, which contains the README.md file.
3. Run the program as a module: `python -m converter -h`. This will print the help message.
4. Run the program as a module with real inputs: `python -m converter <input_filepath> <output_dirpath> <corr_threshold> <is_directed> <get_coords>`
   For input, i.e. `python -m converter data/era5_sst_011940_122022_globe.nc out 0.7 no no 100`

### converter Usage:

```commandline
usage: python -m converter [-h] input_filepath output_dirpath

positional arguments:
  input_filepath     Input File Pathname
  output_dirpath     Output Directory Pathname
  corr_threshold     Node Feature Correlation Threshold
  is_directed        If Directed Graphs: `yes` or `no`
  get_coords         If Output Coordinates: `yes` or `no`
  min_edges          Minimum Number of Edges for All Nodes

optional arguments:
  -h, --help  show this help message and exit
```

## Major Updates

1. On May 13, 2023, the measure was changed from the Pearson correlation coefficient to the Kendall rank correlation coefficient.
2. On July 2, 2023, the minimum number of edges was added, which generated up to the minimum number of edges to a node if the number of current edges to the node is smaller than the minimum.

## Major Applications

1. The program was used to generate graphs for [our paper to the ICLR 2023 Workshops](https://www.climatechange.ai/papers/iclr2023/39).
