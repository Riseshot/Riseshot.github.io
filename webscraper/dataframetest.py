import pandas as pd
import unicodedata
from bs4 import BeautifulSoup
import requests
import urllib.parse



# html_doc = """\
# <div class='ah-content'>
#   <h4>XYZ Community</h4>
#   <p>123 Street</p>
#   <p>Atlanta, Georgia, 12345</p>
#   <p>1234567890</p>
#  </div>

# <div class='ah-content'>
#   <h4>ABC Community</h4>
#   <p>456 Street</p>
#   <p>Miami, Florida, 12345</p>
#   <p>2345678901</p>

#  </div>


#  """

dirty_html = """\
<div class=\ "entry clearfix\"> \n\t\t\t\t\t\t<img class=\ "emoticon\" src=\ "https:\/\/salaries.archinect.com\/assets\/images\/emoticon-7.png\" width=\ "30\" height=\ "30\" border=\ "0\" alt=\ "Job Satisfaction\" data-original-title=\ "Job Satisfaction (1-10): 7\">\n\t\t\t\t\t
  <h3>
<span class=\"salary\">AUD&#36;128<span>per year<\/span><\/span><span class=\"slash\">&nbsp;<\/span>Melbourne, AU<span class=\"slash\">&nbsp;<\/span>Senior Architect<\/h3>\n                        
<ul class=\"subcol subcol-1\">
<li>Corporate<\/li>
<li>201-500 People<\/li>
<li>No Overtime<\/li>
<li>20 Days Vacation<\/li>
<li>
   AUD&#36;3,000 Bonus<\/li>\n                        <\/ul>\n                        \n                        
   <ul class=\"subcol subcol-2\">
   \n                            
<li>Full-time<\/li>\n                            
<li>11-15 Years of Experience<\/li>\n                            
<li>31-35 Years old<\/li>\n                            
<li>Male<\/li>
<li>
   Licensed<\/li>\n                        <\/ul>\n                        \n                        
   <ul class=\"subcol subcol-3\">
   \n                            \n                        <\/ul>\n\t\t\t
   <div class=\"date-stamp\">
   <span>Jun '22<\/span><\/div>\n                    <\/div>


"""
# string = dirty_html
html_doc = dirty_html.replace("\/" , "/")

soup = BeautifulSoup(html_doc, "html.parser")

# strings = [[t.text for t in c.find_all()] for c in soup.select(".ah-content")]

# df = pd.DataFrame(strings, columns=["Name", "Address", "Address2", "Phone"])
# print(df)

match = soup.find('h3')
matchtext = match.text
#unicodeconvert = unicodedata.normalize("NFKD", matchtext)
match2 = [soup.find('div', class_='date-stamp').text]

match3 = soup(text=lambda t:"Years of Experience" in t.text)
match4 = soup(text=lambda t:"Years old" in t.text)


salary_location_position = matchtext.split(u'\xa0') + match2 + match3 + match4

location = matchtext.split(u'\xa0')[1]


url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(location) +'?format=json'

response_location = requests.get(url).json()


match5 = response_location[0]["lat"]
match6 = response_location[0]["lon"]


salary_location_position_gps = matchtext.split(u'\xa0') + match2 + match3 + match4 + [match5] + [match6]

print(match5)
print(location)
print(salary_location_position_gps)
# print(matchtext)
# print(match2)
# print(match3)
# print(match4)
# print(salary_location_position)
