import urllib.request
import re
from functools import cmp_to_key

website_url = 'https://www.cdph.ca.gov'
main_page_url = website_url + '/Programs/OPA/Pages/New-Release-2020.aspx#'

def get_webpage_content(url):
	# return str html
	try:
		req = urllib.request.Request(url)
		response = urllib.request.urlopen(req)
		webpage_str = response.read()
		return str(webpage_str)
	except Exception as e:
		print("error reading:" + url)
		raise

def get_latest_date(s1, s2):
	d1 = re.findall("/Programs/OPA/Pages/NR20-(\d+).aspx", s1)[0]
	d2 = re.findall("/Programs/OPA/Pages/NR20-(\d+).aspx", s2)[0]
	return int(d1) - int(d2)

def get_lastest_page_info(latest_webpage_str):
	print("get page info")
	date = re.findall(r"Date:\s+(.*),\s+2020<br/>", latest_webpage_str)
	positive_cases = re.findall(r"([,\d]+) [\\\d\w]+ Positive cases</p>", latest_webpage_str)
	death = re.findall(r"<p>([,\d]+) \\xe2\\x80\\x93 Deaths", latest_webpage_str)
	pending = re.findall(r" At least ([,\d]+) results have been received and another ([,\d]+) are pending.", latest_webpage_str)
	return date[0] if len(date) > 0 else None, positive_cases[0] if len(positive_cases) > 0 else None, death[0] if len(death) > 0 else None, pending[0] if len(pending) else None

# find all occurences of /Programs/OPA/Pages/NR.*.aspx
all_urls = re.findall(r"(/Programs/OPA/Pages/NR20-\d+.aspx)", get_webpage_content(main_page_url))
all_urls = sorted(all_urls, key=cmp_to_key(get_latest_date))

# get latest page content
latest = all_urls[-1]
latest_webpage_str = get_webpage_content(website_url + latest)

# parse the content
print(get_lastest_page_info(latest_webpage_str))

# for url in all_urls:
# 	print(url)
	# print(get_lastest_page_info(get_webpage_content(website_url + url)))	