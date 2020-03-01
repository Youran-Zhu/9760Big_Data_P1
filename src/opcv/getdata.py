
from sodapy import Socrata
import json

def get_data(page_size, num_pages, output):
    client = Socrata("data.cityofnewyork.us", "io7xTnlVGyUEHLw5g4QflUqph")
    offset = 0
    res = []
    f = open("data.json", "w")
    for i in range(num_pages):
        one_page = client.get("nc67-uf89", limit=page_size, offset=offset)
        for item in one_page:
            res.append(item)
        offset += page_size
    if output:
        print(res)
    else: 
        json.dump(res, f)



