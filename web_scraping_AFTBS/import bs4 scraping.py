import bs4, requests

def getxkcdImage(imageUrl):
	res = requests.get(imageUrl)
	res.raise_for_status()

	soup = bs4.BeautifulSoup(res.text, 'html.parser')
	elems =soup.select('//*[@id="comic"]/img')
	return elems[0].text.strip


	image = getxkcdImage('https://xkcd.com/2154/')
	print('The image is ' + image)	

