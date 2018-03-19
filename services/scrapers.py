'''
scraper for getting the captions files for youtube videos
'''

from bs4 import BeautifulSoup
import urllib as urllib2
import requests

# Don't bother using these two
srtBaseUrl = "https://downsub.com/"
srtLink = "https://downsub.com/?url=https%3A%2F%2F"

diycaptionsBase = "http://diycaptions.com/php/get-automatic-captions-as-txt.php?id="

demoYouTubeLink = "https://www.youtube.com/watch?v=WjkRdgQNGec"

# We're not using this
# The DIYcaptions one works better
def getSrtFromLink(url):
	request = requests.get(srtLink + url)
	data = request.text
	soup = BeautifulSoup(data)

	# for link in soup.find_all('a'):
	# 	# print(link)
	# 	print(link.get('href'))
	downUrl = srtBaseUrl + soup.find_all('a')[1].get('href')[2:]
	print(downUrl)
	resp = requests.get(downUrl, stream=True)
	# req = urllib2.Request(downUrl)
	# res = urllib2.urlopen(rq)
	# srt = open("files/" + name, 'wb')
	# srt.write(res.read())
	# srt.close()
	if resp.status_code == 200:
		with open("./files/file1.srt", 'wb') as f:
			f.write(resp.content)
	return "hello"

# TODO add conditions for en and asr
def getCaptionText(youtubeUrl):
	vid = youtubeUrl.split('?')[1][2:]
	reqUrl = diycaptionsBase + vid + '&language=asr'
	request = requests.get(reqUrl)
	data = request.text
	soup = BeautifulSoup(data)
	content = str(soup.find_all('div')[1]).split('<br/>')[-1].replace('</div>', '')
	# print(content)
	return content

# Add full stops randomly to text which doesn't have punctuated captions
# LOL
def addStops(content, skipWords = 25):
	s = ''
	for idx, word in enumerate(content.split(' ')):
		if idx%skipWords == 0:
			s += word + '. '
			continue
		s += word + ' '
	
	return s
	# return "hello"


if(__name__) == "__main__":
	print(addStops(getCaptionText(demoYouTubeLink)))
