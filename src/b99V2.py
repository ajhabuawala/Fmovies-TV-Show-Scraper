
'''

Simple Episode Tracker in Python from free online tv show site Fmovies

'''

from bs4 import BeautifulSoup 
from urllib.request import urlopen, Request
import time 

#Get HTML 
def get_html(url):
	req = Request(url,  headers={'User-Agent': 'Mozilla/5.0'} )
	server = urlopen(req)
	page_html= server.read()
	server.close()
	soup = BeautifulSoup(page_html,'html.parser')
	name = (soup.h1).get_text()
	return (soup, name)
	


#Extracting the Episode list
def get_episodes(raw_html):
	my_cloud =raw_html.findAll('div',{'data-id':'28'})
	episodes = len(my_cloud[0].findAll('li'))
	return episodes



start_time = time.time()

with open('fav_tvshows.txt', 'r') as f:
	for url in f:
		raw_html, name = get_html(url)
		episodes = get_episodes(raw_html)
		print("The Latest Episode Of {} is Episode {}".format(name,episodes))


print("--- %s seconds ---" % (time.time() - start_time))




	

