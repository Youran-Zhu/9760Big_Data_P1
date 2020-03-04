from sodapy import Socrata
import json

def get_data(app_key,page_size, num_pages, output_file):
    client = Socrata("data.cityofnewyork.us", app_key)
    offset = 0
    res = []
    # If num_pages is not provided, calculate the num_pages so that we can read the entire content.
    if num_pages is None:
        total_records = int(client.get("nc67-uf89", select="COUNT(*)")[0]["COUNT"])
        num_pages = total_records // page_size + 1
    #load Json_file is output is provided
    if output_file is not None:
    	#f = open(output_file, "w")
        f = open(output_file, 'a')
    # Get records        
    for i in range(num_pages):
        one_page = client.get("nc67-uf89", limit=page_size, offset=offset)
        if output_file is None:
            print(one_page)
        else:
            for item in one_page:
                f.write(json.dumps(item) + '\n')
        offset += page_size

    if output_file is not None:
        f.close()
    
    # data = json.loads(f)
    # print(data)


