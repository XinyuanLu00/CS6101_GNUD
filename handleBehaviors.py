##This file is an extraction for MIND features, i.e. News_Users and News_Users
import pandas as pd 
import json
import numpy


##This is the function for getting user_news relations
def getUserNews(df):
	user_news_dict = dict()
	for row in df.itertuples():
		user = getattr(row, 'user')
		impressions = getattr(row, 'impressions')
		imp = impressions.split()
		key = int(user[1:])
		value = []
		for ii in imp:
			if ii.endswith('-1'):
				newid = int(ii.split('-')[0][1:])
				value.append(newid)

		if key in user_news_dict:
			origin_value = user_news_dict.get(key)
			new_value = list(set(origin_value + value))
			user_news_dict[key] = new_value
		else:
			user_news_dict[key] = value

	return user_news_dict

##This is the function for getting the news_user relations
def getNewsUser(df):
	news_user_dict = dict()
	for row in df.itertuples():
		user = getattr(row, 'user')
		impressions = getattr(row, 'impressions')
		imp = impressions.split()
		value = [int(user[1:]),]
		keys = []
		for ii in imp:
			if ii.endswith('-1'):
				newid = int(ii.split('-')[0][1:])
				keys.append(newid)

		for key in keys:
			if key in news_user_dict:
				origin_value = news_user_dict.get(key)
				new_value = list(set(origin_value + value))
				news_user_dict[key] = new_value

			else:
				news_user_dict[key] = value

	return news_user_dict

##main function

def main():
	df = pd.read_csv('behaviors.tsv', sep='\t', names=['id', 'user', 'time', 'history', 'impressions']) ## read data from behaviors in MIND
	user_news_dict = getUserNews(df)
	news_user_dict = getNewsUser(df)

	key_order = sorted(user_news_dict.keys())

	res_un = []
	res_un.append([])
	for key in key_order:
		res_un.append(user_news_dict[key])

	with open('user_news_dict.txt', 'w') as txt_file:
			txt_file.write(str(res_un))

	json_str = json.dumps(news_user_dict)
	with open('news_user_dict.json', 'w') as json_file:
		json_file.write(json_str)

if __name__ == '__main__':
	main()
