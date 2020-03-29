from parse_ca_data import Scrapper
from util import my_print
import re
from functools import cmp_to_key

website_url = 'https://www.cdph.ca.gov'
main_page_url = website_url + '/Programs/OPA/Pages/New-Release-2020.aspx#'

def main():
	scrapper = Scrapper()
	# find all occurences of /Programs/OPA/Pages/NR.*.aspx
	all_urls = re.findall(r"(/Programs/OPA/Pages/NR20-\d+.aspx)", scrapper.get_webpage_content(main_page_url))
	all_urls = sorted(all_urls, key=cmp_to_key(scrapper.get_latest_date))

	# get latest page content
	latest = all_urls[-3]
	latest_webpage_str = scrapper.get_webpage_content(website_url + latest)

	dedup_url = {}
	for url in all_urls[-10:]:
		if url not in dedup_url:
			dedup_url[url] = True
			my_print(url)
			content = scrapper.get_webpage_content(website_url + url)
			if content:
				# print(content)
				print(scrapper.get_lastest_page_info(content))
main()