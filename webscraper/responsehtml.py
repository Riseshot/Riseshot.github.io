r = session.get('http://python-requests.org/')

r.html.render()

r.html.search('Python 2 will retire in only {months} months!')['months']
