from datetime import datetime
from elasticsearch import Elasticsearch
from requests import get
from time import sleep

def create_and_update_index(index_name):
	es = Elasticsearch()
	try:
		es.indice.create(index = index_name)
	except Exception:
		pass

	return es


def clean_record(record):
	violation_timeframe = 'no_record'
	for k,v in record.items():
		# change string to floats 
		if 'amount' in k:
			record[k] = float(v)
		# find date 
		if k == 'issue_date':
			violation_date = v
		# find AM/PM 
		if k == 'violation_time':
			violation_timeframe = v[-1] + 'M'
	# Change string to python understandable time	
	# leap year exception
	try: 
		violationdate = datetime.strptime(violation_date,'%m/%d/%Y').date()
	except:
		mon, day, year = map(int, violation_date.split('/'))
		if (year % 4 != 0) or (year % 100 ==0 and year %400 !=0):
			if mon == 2 and day == 29:
				mon, day = 3, 1
				violationdate = datetime.date(year, mon, day)
	record["violation_date"] = violationdate

	#add AM/PM
	if violation_timeframe != 'no_record':
		record["violation_timeframe"] = violation_timeframe
	else:
		record["violation_timeframe"] = 'N/A'

	return record

def load_elasticsearch(es, index, record):
	record_clean = clean_record(record)
	res = es.index(index = index, body=record_clean,
				   id=record_clean['summons_number'])
	print(res['result'])





