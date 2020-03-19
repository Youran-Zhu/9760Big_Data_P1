from sodapy import Socrata
import json
from src.opcv.elastic_search import create_and_update_index,load_elasticsearch

def get_data(app_key,page_size, num_pages, output_file):
    client = Socrata("data.cityofnewyork.us", app_key)
    res = []
    # If num_pages is not provided, calculate the num_pages so that we can read the entire content.
    if num_pages is None:
        total_records = int(client.get("nc67-uf89", select="COUNT(*)")[0]["COUNT"])
        num_pages = total_records // page_size + 1
    #load Json_file is output is provided
    if output_file is not None:
        f = open(output_file, 'a')
    #load elasticsearch
    es = create_and_update_index('opcv_bigdata')
    # Get records        
    for i in range(num_pages):
        one_page = client.get("nc67-uf89", limit=page_size, offset= i*page_size)
        #output records depending on client requests
        if output_file is not None:
            for record in one_page:
                f.write(json.dumps(record) + '\n')
        #push record to elasticsearch 
        for record in one_page:
            load_elasticsearch(es, 'opcv_bigdata', record)

    if output_file is not None:
        f.close()
        
