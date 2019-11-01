import sys
import re
import random
import time
from bs4 import BeautifulSoup
from robobrowser import RoboBrowser
import csv

filename = sys.argv[1]
className = sys.argv[2]

agent = ['Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:70.0) Gecko/20100101 Firefox/70.0',
         'Mozilla/5.0 (Linux; Android 7.0; FRD-L02) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Mobile Safari/537.36'
         ]
parser = 'html.parser'
browser = RoboBrowser(history=False,
                      user_agent=random.choice(agent),
                      parser=parser)
links_to_scrape = []
img_links = []
# Give  target url file
with open(filename, 'r') as csvFile:
	target = csv.reader(csvFile)
	for row in target:
		links_to_scrape.append(row[0])
for profile in links_to_scrape:
	url = profile
	print url
	browser.open(url)

	# Give the class for image div for extract images
	html_doc = browser.find_all("div", {"class": className})
	soup = BeautifulSoup(str(html_doc), 'html.parser')
	images = soup.findAll('img')
	print images
	for image in images:
		img_links.append(image['src'])
		print image['src']
	# File to save the image urls
	with open('images.csv','a') as f:
	    for item in img_links:
	    	f.write(url + "," + item)
	    	f.write('\n')




