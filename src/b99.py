#! /usr/bin/python3.5

'''
Simple Episode Tracker in Python from free online tv show site Fmovies

'''

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen, Request



#Brooklyn 99 Season 5 Fmovies.se link
url = 'https://www5.fmovies.se/film/brooklyn-nine-nine-5.kk3nr/yrqv1z'

#Get HTML 
req = Request(url,  headers={'User-Agent': 'Mozilla/5.0'} )
server = urlopen(req)
page_html= server.read()
server.close()
raw_html = soup(page_html,'html.parser')
print(raw_html.h1)

#Extracting the Episode list
my_cloud =raw_html.findAll('div',{'data-id':'28'})
episodes = len(my_cloud[0].findAll('li'))

print("The Latest Episode Of Brooklyn Brooklyn-Nine-Nine-S5 is Episode {}".format(episodes))


	

