from pathlib import Path
import argparse

from converter.process_files import *

# Argument parser
arg_parser = argparse.ArgumentParser()
arg_parser.add_argument("input_filepath", type=str,
                        help="Input File Pathname")
arg_parser.add_argument("output_dirpath", type=str,
                        help="Output Directory Pathname")
args = arg_parser.parse_args()

input_filepath = Path(args.input_filepath)
output_dirpath = Path(args.output_dirpath)

# Read the input, process the input, and write the output.
process_files(input_filepath, output_dirpath)