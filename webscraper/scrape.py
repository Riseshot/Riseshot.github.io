from bs4 import BeautifulSoup
import requests

from requests_html import HTMLSession
s = HTMLSession()
response = s.get('https://salaries.archinect.com/poll/results/all/view-all')
response.html.render(wait=0.1, sleep=3)

#source = requests.get('https://salaries.archinect.com/poll/results/all/view-all')
soup = BeautifulSoup('response', 'lxml')

#print(soup.prettify())

div = soup.select('div' , class_='span8 column co1-2')


#divc = div[1]

#rows = soup.select('div' , class_='span8 column co1-2')

entry = soup.select('div' , class_='entry clearfix')

odd = soup.find('span' , class_='salary')



salary = div

print(salary)