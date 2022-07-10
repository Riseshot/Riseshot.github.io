from requests_html import HTML, HTMLSession

# with open('simple.html') as html_file:
# 	source = html_file.read()
# 	html = HTML(html=source)
	
session = HTMLSession()
r = session.get('https://salaries.archinect.com/poll/results/all/view-all')
r.html.render(wait=0.1, sleep=2)


print(r.html.html)