import requests
import pandas as pd
import unicodedata
from bs4 import BeautifulSoup
import urllib.parse

url = "https://salaries.archinect.com/salarypoll/results"

res =[]
for x in range(0,3):
    querystring = {"sEcho":"2","iColumns":"2","sColumns":"","iDisplayStart":f"{10 * x + 20}","iDisplayLength":"10","mDataProp_0":"0","mDataProp_1":"1","sSearch":"","bRegex":"false","sSearch_0":"","bRegex_0":"false","bSearchable_0":"false","sSearch_1":"","bRegex_1":"false","bSearchable_1":"true","iSortCol_0":"0","sSortDir_0":"asc","iSortingCols":"1","bSortable_0":"true","bSortable_1":"false","age":"[]","gender":"[]","job_title":"[]","primary_market":"[]","experience":"[]","firm_type":"[]","firm_size":"[]","work_status":"[]","license":"[]","health_insurance":"[]","overtime":"[]","annual_bonus":"[]","sort_by":"id","salary-range":"0;100000","range_plus":"true","location":"","under_graduate_school":"","graduate_school":"","post_graduate_school":"","location_type":"all","salary_time":"[]","job_satisfaction":"[]","_":"1657203422691"}

    payload = ""
    headers = {
        "cookie": "ci_session=a%253A5%253A%257Bs%253A10%253A%2522session_id%2522%253Bs%253A32%253A%2522e8e5fa61b92f28644328a855165248ed%2522%253Bs%253A10%253A%2522ip_address%2522%253Bs%253A12%253A%252224.238.62.50%2522%253Bs%253A10%253A%2522user_agent%2522%253Bs%253A111%253A%2522Mozilla%252F5.0%2B%2528Windows%2BNT%2B10.0%253B%2BWin64%253B%2Bx64%2529%2BAppleWebKit%252F537.36%2B%2528KHTML%252C%2Blike%2BGecko%2529%2BChrome%252F103.0.0.0%2BSafari%252F537.36%2522%253Bs%253A13%253A%2522last_activity%2522%253Bi%253A1657203998%253Bs%253A9%253A%2522user_data%2522%253Bs%253A0%253A%2522%2522%253B%257D470d6784d24f74782df6afd2a7ee6db7; PHPSESSID=kofsaeqkhleveiebrbrjasn272",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7",
        "Connection": "keep-alive",
        "Cookie": "PHPSESSID=b3uha9crbf96d52l5pe92lruo4; ci_session=a%3A5%3A%7Bs%3A10%3A%22session_id%22%3Bs%3A32%3A%2290d67c6b0031a770e056f5140bcba991%22%3Bs%3A10%3A%22ip_address%22%3Bs%3A12%3A%2224.238.62.50%22%3Bs%3A10%3A%22user_agent%22%3Bs%3A111%3A%22Mozilla%2F5.0+%28Windows+NT+10.0%3B+Win64%3B+x64%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F103.0.0.0+Safari%2F537.36%22%3Bs%3A13%3A%22last_activity%22%3Bi%3A1657203402%3Bs%3A9%3A%22user_data%22%3Bs%3A0%3A%22%22%3B%7D7a97de25ef2d1a875f25bc4cc1ab8dd3",
        "DNT": "1",
        "Referer": "https://salaries.archinect.com/poll/results/all/view-all",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",

    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    
    
    data = response.json()
    # print(type(data))
    #print(len(data['aaData']))



    for p in data['aaData']:
        res.append(p)

# print(len(res))



df = pd.DataFrame(res)

col_one_list = df[1].tolist()

# df = dfraw.iloc[:, 1]



results = []

i = 0

for i in range(0,len(col_one_list) - 1):
    html = col_one_list[i]
    html_doc = html.replace("\/" , "/")
    soup = BeautifulSoup(html_doc, "html.parser")
    match = soup.find('h3')
    try:
        matchtext = match.text
        match2 = [soup.find('div', class_='date-stamp').text]

        match3 = soup(text=lambda t:"Years of Experience" in t.text)
        match4 = soup(text=lambda t:"Years old" in t.text)

        # salary_location_position_date_yoe_age = matchtext.split(u'\xa0') + match2 + match3 + match4

        location = matchtext.split(u'\xa0')[1]


        url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(location) +'?format=json'

        response_location = requests.get(url).json()


        match5 = response_location[0]["lat"]
        match6 = response_location[0]["lon"]


        salary_location_position_gps = matchtext.split(u'\xa0') + match2 + match3 + match4 + [match5] + [match6]

        #print(salary_location_position_date_yoe_age)
    except:
        continue
        # salary_location_position = "none"

    

    
    #print(salary_location_position)
    results.append(salary_location_position_gps)
    



dfedit = pd.DataFrame(results)

# dfedit.to_csv('firstresults.csv')




print(dfedit)