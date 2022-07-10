from requests_html import HTML

with open('simple.html') as html_file:
	source = html_file.read()
	html = HTML(html=source)
	html.render()
	
# articles = html.find('div.article')
# for article in articles:

# 	headline = article.find('h2', first=True)
# 	summary = article.find('p', first=True)

# 	print(headline.html)
# 	print(summary.html)
# 	print()

match = html.find('#footer', first=True)
print(match.html)
