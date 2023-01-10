# Geo Spatiotemporal Grid to Graph Converter

This program converts a geographic spatiotemporal grid into a graph. This project is under development.

## Programming Language

Python 3.7.15

## Running converter

1. Make sure Python has been installed on your computer.
2. Navigate to [this](.) directory, which contains the README.md file.
3. Run the program as a module: `python -m converter -h`. This will print the help message.
4. Run the program as a module with real inputs: `python -m converter <input_filepath> <output_dirpath>`
   For input, i.e. `python -m converter data/example.nc out`

### converter Usage:

```commandline
usage: python -m converter [-h] input_filepath output_dirpath

positional arguments:
  input_filepath     Input File Pathname
  output_dirpath     Output Directory Pathname

optional arguments:
  -h, --help  show this help message and exit
```