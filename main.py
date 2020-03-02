import argparse
import sys
from src.opcv.getdata import get_data

if __name__ == '__main__':
    ## Take arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("--page_size", help="how many records to request from the API per call", type=int)
    parser.add_argument("--num_pages", help="how many calls we make", type=int)
    parser.add_argument("--output", help=" if not provided, your script should print results to stdout; if provided, your script should write the data to the file", type=str)
    
    args = parser.parse_args()
    page_size = args.page_size
    num_pages = args.num_pages
    output_file = args.output

	get_data(page_size,num_pages,output)
	
