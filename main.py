import sys
from src.opcv.getdata import get_data

if __name__ == '__main__':
	args = sys.argv[1:]
	page_size = int(args[0])
	try:
		num_pages = int(args[1])
	except:
		num_pages = 1
	try:
		output = args[2]
	except:
		output = None

	get_data(page_size,num_pages)
	
