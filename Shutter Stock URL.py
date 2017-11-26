import sys, urllib2, re
from BeautifulSoup import BeautifulSoup

f = open("links.txt", 'w')

url = raw_input("Enter url: ")
#url = "https://www.shutterstock.com/search?search_source=base_landing_page&language=en&searchterm="+ search_word +"&image_type=all"
text = urllib2.urlopen(url).read()
soup = BeautifulSoup(text)

data = soup.findAll('div',attrs={'class':'overlay'})
for div in data:
    links = div.findAll('a')
    for a in links:
    	links = a["href"]
    	links = str(links)
    	if(links.startswith("/image-")):
        	# print "https://www.shutterstock.com" + a['href'] + "\n"
        	f.write("https://www.shutterstock.com" + a['href'] + "\n")

f.close()
