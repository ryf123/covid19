import urllib.request
import re
from util import my_print

class Scrapper:
	def get_webpage_content(self, url):
		# return str html
		try:
			req = urllib.request.Request(url)
			response = urllib.request.urlopen(req)
			webpage_str = response.read()
			return str(webpage_str)
		except Exception as e:
			my_print("error reading:" + url)
			return None

	def get_latest_date(self, s1, s2):
		d1 = re.findall("/Programs/OPA/Pages/NR20-(\d+).aspx", s1)[0]
		d2 = re.findall("/Programs/OPA/Pages/NR20-(\d+).aspx", s2)[0]
		return int(d1) - int(d2)

	def get_lastest_page_info(self, latest_webpage_str):
		my_print("get page info")
		date = re.findall(r"Date:\s+(.*),\s+2020<br/>", latest_webpage_str)
		positive_cases = re.findall(r"([,\d]+)[\\\d\w\s]+Positive cases", latest_webpage_str)
		death = re.findall(r"([,\d]+)[\\\d\w\s]+Deaths", latest_webpage_str)
		pending = re.findall(r" least ([\+,\d]+) results have been received and another ([\+,\d]+) are pending", latest_webpage_str)
		return {
			'date': date[0] if len(date) > 0 else None,
			'positive_cases': positive_cases[0] if len(positive_cases) > 0 else None,
			'death': death[0] if len(death) > 0 else None,
			'results received': pending[0][0] if len(pending) else None,
			'results pending': pending[0][1] if len(pending) else None
		}