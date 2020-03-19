# NYC Parking Violations

In this project, we are going to load and then analyze a dataset containing millions of NYC parking violations since January 2016. The data is from NYC OPEN DATA website and API is from Socrata Open Data API. 

## Part I 
In Part I, I will develop a python command line interface that can connect to the OPCV API and demonstrate that the data is accessible via python.

### 1) File Structure
```
root folder: part1 
     contains files: Dockerfile; README.md; main.py; requirement.txt; result.json
     contains folder:src
opcv/src
     contains folder: opcv
opcv/src/opcv 
     contains file: getdata.py
```

### 2) File Detail
#### i) Python scripting:
```
  a) getdata.py
    It contains code that creates function get_data(app_key,page_size, num_pages, output_file), using API Socrata from            sodapy 

  b) main.py
   It takes input app_key, and parses inputs: --page_size, --num_pages, --output to feed to get_data(). And then execute         the function get_data().
   > app_key, --page_size, --num_pages are required inputs. --num_pages, --output are optional inputs.
   > Users can call -h for help
   > app_key: This is user's APP_KEY for the API.
     --page_size: This is how many records to request from the API per call.
     --num_pages: If not provided, it will request data until the entirety of the content has been exhausted. 
                  If provided, it will query for data num_pages times.
     --output: If not provided, it will print results to stdout. 
               If provided, it will write the data to the file.
```                 
#### ii) Docker Support File:
```
  a) Dockerfile
     It builds docker image

  b) requirement.txt
     It specifys what package to for docker to download in order to run the code.
```      
#### iii) Sample Output:
```
  a) result.json
     It contains 8 records extracted from the dataset, using arguements --page_size=2, --num_pages=4, --output=result.json
``` 

### 3) Dockerhub 
Build immage
```
  docker build -t bigdata1:1.0 .
```
Get UUID
```
  docker images | grep bigdata1
```
Tag the image with dockerhub information
```
  docker tag {UUID} fedoooooo/bigdata1:1.0 
```
Push to dockerhub
```
  docker push fedoooooo/bigdata1
```
## Part II
In Part II, I used docker-compose to spin up a service that encapsulates bigdata1 container and an elasticsearch container.
I update the original script (from Part 1) to now not only download the data but also load it into elasticsearch instance.

### 1) File Structure and Updates
Comparing with part I, I added three following files in Part II folder. I also added elastic search related package in requirement.txt

```
1) docker-compose.yml
   Code to build docker-compose

2) elastic_search.py
   Elastic search helper function

3) curl_output.txt
   Curl request output from "curl -o curl_output.txt http://localhost:9200/opcv_bigdata/_search?size=10&pretty=true"
```
### 3) Docker-compose & elastic search commend line

1) Build Pyth, Elastic Search and Kibana instances
```
docker-compose build pyth
```
2) Lauch these services
```
docker-compose up -d
```
3) Run main.py script to push to elastic search 
```
docker-compose run -e APP_KEY={api_key} -v ${PWD}:/app pyth python main.py --page_size=74 --num_pages=1 --output=results.json
```
4) Kill the services if needed
```
docker-compose down
```
5) Using curl to request our data loaded into ElasticSearch  
```
curl -o curl_output.txt http://localhost:9200/opcv_bigdata/_search?size=10&pretty=true
```

## Part III
I loaded 50,000 records into ElasticSearch. In this part, I visualized these records with Kibana

![Counts of different fine amount vs Violation Type
(https://github.com/Youran-Zhu/9760Big_Data_P1/blob/master/part3/count_fineAmount_violationType.png)

