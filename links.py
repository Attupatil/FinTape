# get links froma a string
# from FinTape.py import url_string
import re
import requests
from bs4 import BeautifulSoup
import json

def links_r(url_string):
	listToStr = ' '.join([str(elem) for elem in url_string])
	# s = 'This is my tweet check it out http://tinyurl.com/blah and http://blabla.com'
	s = re.findall(r'(https?://\S+)', listToStr)
	return s
	# print(s)
	# replace the URL with the page you want to scrape
	text =[]
	for url in s:
		def print_headlines(response_text):
		    soup = BeautifulSoup(response_text, 'lxml')
		    headlines = soup.find_all(attrs={"itemprop": "headline"})
		    for headline in headlines:
		        print(headline.text)


		def get_headers():
		    return {
		        "accept": "*/*",
		        "accept-encoding": "gzip, deflate, br",
		        "accept-language": "en-IN,en-US;q=0.9,en;q=0.8",
		        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
		        "cookie": "_ga=GA1.2.474379061.1548476083; _gid=GA1.2.251903072.1548476083; __gads=ID=17fd29a6d34048fc:T=1548476085:S=ALNI_MaRiLYBFlMfKNMAtiW0J3b_o0XGxw",
		        "origin": "https://inshorts.com",
		        "referer": "https://inshorts.com/en/read/",
		        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
		        "x-requested-with": "XMLHttpRequest"
		    }


		# url = 'https://inshorts.com/en/read'
		response = requests.get(url)
		print_headlines(response.text)

		# get more news
		# url = 'https://inshorts.com/en/ajax/more_news'
		news_offset = "apwuhnrm-1"

		while True:
		    response = requests.post(url, data={"category": "", "news_offset": news_offset}, headers=get_headers())
		    if response.status_code != 200:
		        print(response.status_code)
		        break

		    response_json = json.loads(response.text)
		    print_headlines(response_json["html"])
		    news_offset = response_json["min_news_id"]
		    




	#     # url = 'https://www.example.com'

	#     # send a GET request to the URL and get the HTML content
	#     response = requests.get(url)
	#     html_content = response.content

	#     # create a BeautifulSoup object to parse the HTML content
	#     soup = BeautifulSoup(html_content, 'html.parser')

	#     # find all the headline tags (h1, h2, h3, etc.) and extract the text
	#     headlines = [headline.text for headline in soup.find_all(['h1'])]   #, 'h2', 'h3', 'h4', 'h5', 'h6'

	#     # display the headlines
	#     for headline in headlines:
	#         print(headline)
	#         text += headline
	# return text

# def print_headlines(s):
# 	text = []
# 	for x in range(0,3):
# 		soup = BeautifulSoup(s[x], 'lxml')
# 		headlines = soup.find_all(attrs={"itemprop": "headline"})

# 		for headline in headlines:
# 			text += headline.text
# 			print(headline.text)
# 	return text



# # url = 'https://inshorts.com/en/read'
# # response = requests.get(url)
# # print_headlines(response.text)

# import requests
# from bs4 import BeautifulSoup



