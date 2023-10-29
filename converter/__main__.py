from pathlib import Path
import argparse

from converter.process_files import *

# Argument parser
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument('input_filepath', type=str,
                        help='Input File Pathname')
arg_parser.add_argument('output_dirpath', type=str,
                        help='Output Directory Pathname')
arg_parser.add_argument('corr_threshold', type=str,
                        help='Node Feature Correlation Threshold')
arg_parser.add_argument('is_directed', type=str,
                        help="If Directed Graphs: 'yes' or 'no'")
arg_parser.add_argument('get_coords', type=str,
                        help="If Output Coordinates: 'yes' or 'no'")
arg_parser.add_argument('min_edges', type=str,
                        help='Minimum Number of Edges')
args = arg_parser.parse_args()

input_filepath = Path(args.input_filepath)
output_dirpath = Path(args.output_dirpath)
corr_threshold = Path(args.corr_threshold)
is_directed = Path(args.is_directed)
get_coords = Path(args.get_coords)
min_edges = Path(args.min_edges)

# Read the input, process the input, and write the output.
process_files(input_filepath, output_dirpath, corr_threshold, is_directed, get_coords, min_edges)