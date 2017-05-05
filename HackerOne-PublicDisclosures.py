import pymongo
import requests
'''
This scripts get the list of all publich disclosures and dumps it into MongoDB
'''
def get_items(cursor):
	for item in cursor:
		print (item)

def get_mongo_conn():
	client = pymongo.MongoClient()
	client.drop_database('h1')
	db = client.h1
	collection = db.dataset
	return collection

def insert_to_db(report):
	#collection = get_mongo_conn()
	type(collection)
	collection.insert_one(report)

def get_reports():
	s = requests.session()
	headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'Accept-Encoding': ', '.join(('gzip', 'deflate')),
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/json',
    'Connection': 'keep-alive',
}
	page = s.get('https://hackerone.com/hacktivity?sort_type=latest_disclosable_activity_at&filter=type%3Apublic&page=1&range=forever',headers=headers)
	no_of_pages = page.json().get('pages') + 1
	#no_of_pages = 3
	for i in range (1,no_of_pages):
		r = s.get('https://hackerone.com/hacktivity?sort_type=latest_disclosable_activity_at&filter=type%3Apublic&page='+str(i)+'&range=forever',headers=headers)
		jsn = r.json()
		for itm in jsn.get('reports'):
			itm['url'] = "https://hackerone.com" + itm['url']
			insert_to_db(itm)



client = pymongo.MongoClient()
#client.drop_database('h1')
db = client.h1
collection = db.dataset
get_reports()
