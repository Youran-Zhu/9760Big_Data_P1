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
    if output_file is not None:
    	f = open(output_file, "w")
    for i in range(num_pages):
        one_page = client.get("nc67-uf89", limit=page_size, offset=offset)
        if output_file is None:
            print(one_page)
        else:
            for item in one_page:
                res.append(item)
                offset += page_size
    if output_file is not None:
        json.dump(res, f)
        f.close()
