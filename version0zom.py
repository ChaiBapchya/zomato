import csv
import requests
from lxml import html
import itertools
import pandas as pd 
import re
#filepath = 'rest.csv'
#writer=csv.writer(open(filepath,'wb'))
#header=['rest_name']
#writer.writerow(header)

def oneDArray(x):
    return list(itertools.chain(*x))



cookies = {
    'fbcity': '3',
    'zl': 'en',
    'fbtrack': '348ec2207b3d6c55a7ca231d677e419a',
    '_ga': 'GA1.2.1124886037.1475382045',
    'dpr': '1',
    'fbm_288523881080': 'base_domain=.zomato.com',
    'zhli': '1',
    'squeeze': 'e6c1d9490c106fc68a20b1907a41e849',
    'orange': '5768794',
    '__utmx': '141625785.FQnzc5UZQdSMS6ggKyLrqQ$0:',
    '__utmxx': '141625785.FQnzc5UZQdSMS6ggKyLrqQ$0:1486207870:8035200',
    'PHPSESSID': '1549cf5ac03934a92c821460668aa0a21c9e8972',
    '__jpuri': 'https%3A//www.zomato.com/mumbai/lunch',
}

headers = {
    'Host': 'www.zomato.com',
    'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:51.0) Gecko/20100101 Firefox/51.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

url = 'https://www.zomato.com/mumbai/lunch?page='
rest_name=[]
rest_type=[]
rest_score=[]
rest_votes=[]
rest_reviews=[]
rest_zone=[]
rest_address=[]
rest_cost=[]
rest_timings=[]
rest_featured_in=[]
rest_call=[]

for i in range(11,14):
	response = requests.get(url+str(i), headers=headers,cookies=cookies)#,cookies=cookies
	
	tree = html.fromstring(response.content)
	page_limit=int(tree.xpath('count(//*[@id="orig-search-list"]/div[*])'))
	print page_limit
	for j in range(1,page_limit):
		rest_type_value = tree.xpath('//*[@id="orig-search-list"]/div['+str(j)+']/div[1]/div/article/div[1]/div/div[2]/div[1]/div[1]/div[1]/*/text()')
		if not rest_type_value:
			rest_type_value=['empty']
		rest_type.append(rest_type_value)
		# rest_name.append(tree.xpath('//*[@id="orig-search-list"]/div[*]/div[1]/div/article/div[1]/div/div[2]/div[1]/div[1]/a[1]/text()'))
		# rest_score.append(tree.xpath('//*[@id="orig-search-list"]/div[*]/div[1]/div/article/div[1]/div/div[2]/div[1]/div[2]/div[1]/text()'))
		# rest_votes.append(tree.xpath('//*[@id="orig-search-list"]/div[*]/div[1]/div/article/div[1]/div/div[2]/div[1]/div[2]/span/text()'))
		# rest_reviews.append(tree.xpath('//*[@id="orig-search-list"]/div[*]/div[1]/div/article/div[1]/div/div[2]/div[1]/div[2]/a/text()'))
		# rest_zone.append(tree.xpath('//*[@id="orig-search-list"]/div[*]/div[1]/div/article/div[1]/div/div[2]/div[1]/div[1]/a[2]/b/text()'))
		# rest_address.append(tree.xpath('//*[@id="orig-search-list"]/div[*]/div[1]/div/article/div[1]/div/div[2]/div[2]/div/text()'))
		# rest_cuisine = tree.xpath('//*[@id="orig-search-list"]/div[*]/div[1]/div/article/div[3]/div[1]/span[2]/*/text()')
		# rest_cost.append(tree.xpath('//*[@id="orig-search-list"]/div[*]/div[1]/div/article/div[3]/div[2]/span[2]/text()'))
		# rest_timings.append(tree.xpath('//*[@id="orig-search-list"]/div[*]/div[1]/div/article/div[3]/div[3]/div[1]/text()'))
		# rest_featured_in.append(tree.xpath('//*[@id="orig-search-list"]/div[*]/div[1]/div/article/div[3]/div[4]/div/*/text()'))
		# rest_call.append(tree.xpath('//*[@id="orig-search-list"]/div[*]/div[2]/a[1]/@data-phone-no-str'))
		
		# if not rest_name:
		# 	rest_name.append('empty')
		# if not rest_score:
		# 	rest_score.append('empty')
		# if not rest_votes:
		# 	rest_votes.append('empty')
		# if not rest_reviews:
		# 	rest_reviews.append('empty')
		# if not rest_zone:
		# 	rest_zone.append('empty')
		# if not rest_address:
		# 	rest_address.append('empty')
		# if not rest_cuisine:
		# 	rest_cuisine.append('empty')
		# if not rest_cost:
		# 	rest_cost.append('empty')
		# if not rest_timings:
		# 	rest_timings.append('empty')
		# if not rest_featured_in:		
		# 	rest_featured_in.append('empty')
		# if not rest_call:	
		# 	rest_call.append('empty')

print rest_type
# print rest_name
# print rest_score
# print rest_votes
# print rest_reviews
# print rest_zone
# print rest_address
# print rest_cost
# print rest_timings
# print rest_featured_in
# print rest_call

## commented all below ########

# #################### convert list of list (2 dimensional) into 1 dimensional .. flattens ###############
# #rest_type=oneDArray(rest_type)
# rest_name=oneDArray(rest_name)
# rest_score=oneDArray(rest_score)
# rest_votes=oneDArray(rest_votes)
# rest_reviews=oneDArray(rest_reviews)
# rest_zone=oneDArray(rest_zone)
# rest_address=oneDArray(rest_address)
# rest_cost=oneDArray(rest_cost)
# rest_timings=oneDArray(rest_timings)
# #rest_featured_in=oneDArray(rest_featured_in)
# rest_call=oneDArray(rest_call)
# ########### strip /n, /t, /r , ' ' #####################

# # for row in rest_name:
# # 	row=re.sub('[\s+]', '', row)
# # 	row=row.strip()
# # 	row=row.replace("\n", "")

# rest_name = [word.encode('utf-8').strip() for word in rest_name]
# rest_score = [word.encode('utf-8').strip() for word in rest_score]
# rest_votes = [word.encode('utf-8').strip() for word in rest_votes]
# rest_reviews = [word.encode('utf-8').strip() for word in rest_reviews]
# rest_zone = [word.encode('utf-8').strip() for word in rest_zone]
# rest_address = [word.encode('utf-8').strip() for word in rest_address]
# rest_cost = [word.encode('utf-8').strip() for word in rest_cost]
# rest_timings = [word.encode('utf-8').strip() for word in rest_timings]
# #rest_featured_in = [word.strip() for word in rest_featured_in]
# rest_call = [word.encode('utf-8').strip() for word in rest_call]

# print 'type'+str(len(rest_type))
# print 'name'+str(len(rest_name))
# print 'score'+str(len(rest_score))
# print 'votes'+str(len(rest_votes))
# print 'rev'+str(len(rest_reviews))
# print 'zon'+str(len(rest_zone))
# print 'add'+str(len(rest_address))
# print 'cos'+str(len(rest_cost))
# print 'timin'+str(len(rest_timings))
# #print 'feat'+str(len())
# print 'call'+str(len(rest_call))


# df = pd.DataFrame({"rest_name":rest_name})

# # type_series = pd.Series(rest_type)
# score_series = pd.Series(rest_score)
# vote_series = pd.Series(rest_votes)
# review_series = pd.Series(rest_reviews)
# zone_series = pd.Series(rest_zone)
# add_series = pd.Series(rest_address)
# cost_series = pd.Series(rest_cost)
# timings_series = pd.Series(rest_timings)
# #feat_in_series = pd.Series(rest_featured_in)
# call_series = pd.Series(rest_call)


# #df["rest_type"]=type_series.values
# df["rest_score"]=score_series.values
# df["rest_votes"]=vote_series.values
# df["rest_reviews"]=review_series.values
# df["rest_zone"]=zone_series.values
# df["rest_address"]=add_series.values
# df["rest_cost"]=cost_series.values
# df["rest_timings"]=timings_series.values
# #df["rest_featured_in"]=feat_in_series.values
# df["rest_call"]=call_series.values


# print df

# df.to_csv('restaurant_zomato_data1.csv')
# # for row in final_list:
# # 	for column in row:
# # 		print column

# #print rest_cuisine
# # print rest_score

# # print rest_type
# # print rest_votes
# # print rest_reviews
# # print rest_zone
# # print rest_address
# # print rest_cost
# # print rest_timings
# # print rest_featured_in
# # print rest_call

# # writer.writerow(actual_data)
