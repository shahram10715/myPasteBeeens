import requests
from bs4 import BeautifulSoup
import pandas as pd


session = requests.Session()
url = "?????????????????????????????????????????????????????????????" #to be edited

# Headers that mimic a browser (taken from the HAR file)
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "Accept-Language": "en-US,en;q=0.9,lt;q=0.8",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "?????????????????????????????????????????????????????", #to be edited
    "Referer": url,
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36",
    "X-MicrosoftAjax": "Delta=true",
    "X-Requested-With": "XMLHttpRequest",
}

# First, GET the page to obtain the initial hidden fields
resp_get = session.get(url, headers=headers)
soup_get = BeautifulSoup(resp_get.text, "html.parser")

# Extract the required hidden input values
viewstate = soup_get.find("input", {"name": "__VIEWSTATE"})["value"]
eventvalidation = soup_get.find("input", {"name": "__EVENTVALIDATION"})["value"]
viewstategenerator = soup_get.find("input", {"name": "__VIEWSTATEGENERATOR"})["value"]

# ------------------------------------------------------------
# 2. Build the POST data payload.
#    The fields are taken from the HAR file; dynamic values are
#    inserted from the GET response.
# ------------------------------------------------------------
post_data = {
    # ASP.NET AJAX required fields
    "ctl00$ScriptManager1": "ctl00$MainContent$UpdatePanel1|ctl00$MainContent$RoundPanelSerch$btnSearch",
    "__EVENTTARGET": "ctl00$MainContent$RoundPanelSerch$btnSearch",
    "__EVENTARGUMENT": "Click",
    "__VIEWSTATE": viewstate,
    "__VIEWSTATEGENERATOR": viewstategenerator,
    "__EVENTVALIDATION": eventvalidation,
    "__ASYNCPOST": "true",
    # Search form fields (only txtMeId is filled with 455)
    # "ctl00$MainContent$RoundPanelSerch$txtMeId": "1500",   this line can also be edited
    "ctl00$MainContent$RoundPanelSerch$txtMeNo": "",
    "ctl00$MainContent$RoundPanelSerch$txtFirstName": "",
    "ctl00$MainContent$RoundPanelSerch$txtLastName": "",
    "MainContent_RoundPanelSerch_ComboMajor_VI": "",
    "ctl00$MainContent$RoundPanelSerch$ComboMajor": "--------",
    "ctl00$MainContent$RoundPanelSerch$ComboMajor$DDDState": '{"windowsState":"0:0:-1:0:0:0:-10000:-10000:1:0:0:0"}',
    "ctl00$MainContent$RoundPanelSerch$ComboMajor$DDD$L$State": '{"CustomCallback":""}',
    "ctl00$MainContent$RoundPanelSerch$ComboMajor$DDD$L": "",
    "MainContent_RoundPanelSerch_ComboImplement_VI": "-1",
    "ctl00$MainContent$RoundPanelSerch$ComboImplement": "----",
    "ctl00$MainContent$RoundPanelSerch$ComboImplement$DDDState": '{"windowsState":"0:0:-1:0:0:0:-10000:-10000:1:0:0:0"}',
    "ctl00$MainContent$RoundPanelSerch$ComboImplement$DDD$L$State": '{"CustomCallback":""}',
    "ctl00$MainContent$RoundPanelSerch$ComboImplement$DDD$L": "-1",
    "MainContent_RoundPanelSerch_comboQualification_VI": "-1",
    "ctl00$MainContent$RoundPanelSerch$comboQualification": "----",
    "ctl00$MainContent$RoundPanelSerch$comboQualification$DDDState": '{"windowsState":"0:0:-1:0:0:0:-10000:-10000:1:0:0:0"}',
    "ctl00$MainContent$RoundPanelSerch$comboQualification$DDD$L$State": '{"CustomCallback":""}',
    "ctl00$MainContent$RoundPanelSerch$comboQualification$DDD$L": "-1",
    "MainContent_RoundPanelSerch_comboGrade_VI": "",
    "ctl00$MainContent$RoundPanelSerch$comboGrade": "--------",
    "ctl00$MainContent$RoundPanelSerch$comboGrade$DDDState": '{"windowsState":"0:0:-1:0:0:0:-10000:-10000:1:0:0:0"}',
    "ctl00$MainContent$RoundPanelSerch$comboGrade$DDD$L$State": '{"CustomCallback":""}',
    "ctl00$MainContent$RoundPanelSerch$comboGrade$DDD$L": "",
    "ctl00$MainContent$DataViewMembers": '{"b":true,"pc":1,"pi":0,"ps":0,"layout":0,"pageSize":10,"endlessPagingMode":1,"aspi":0,"ic":1,"pageCount":1,"pageIndex":0}',
    "DXScript": "1_258,1_139,1_252,1_165,1_175,1_142,1_163,1_171,1_162,1_136,1_244,1_160,1_242,1_166,1_144,1_177,1_152,1_240,1_143",
    "DXCss": "0_1855,1_29,1_32,1_30,0_1857,1_11,0_1778,1_10,0_1780,../StyleSheet/bootstrap.css,../StyleSheet/Style.css,../StyleSheet/owl.theme.default.min.css,../StyleSheet/owl.carousel.min.css,../StyleSheet/fontawesome-all.css,../Images/arm3.png",
}

labels_to_extract = [
    "MainContent_DataViewMembers_IT0_Label118_0",
    "MainContent_DataViewMembers_IT0_Label10_0",
    "MainContent_DataViewMembers_IT0_Label8_0",
    "MainContent_DataViewMembers_IT0_Label14_0",
    "MainContent_DataViewMembers_IT0_Label20_0",
    "MainContent_DataViewMembers_IT0_Label218_0",
    "MainContent_DataViewMembers_IT0_Label318_0",
    "MainContent_DataViewMembers_IT0_Label418_0",
    "MainContent_DataViewMembers_IT0_Label13_0",
]

labels_readable = ['Name', 'license_number', 'membership_number', 'phone_number', 'major', 'last_degree', 'nezarat', 'tarahi', 'ejra', 'shahrsazi']


table1 = []

for i in range(1,4001):
    row = []
    print(f'member id {i} is processing...')
    post_data.update({"ctl00$MainContent$RoundPanelSerch$txtMeId": str(i)})
    resp_post = session.post(url, data=post_data, headers=headers)
    soup = BeautifulSoup(resp_post.text, "html.parser")
    name_element = soup.find('span', class_='TitleOragne')
    if name_element:
        row.append(name_element.text)
        for label_id in labels_to_extract:
            element = soup.find(id=label_id)
            text = element.get_text(strip=True)
            row.append(text)
    if row:
        print(f'row number {i} added to the table')
        table1.append(row)



df = pd.DataFrame(table1, columns=labels_readable)
df.to_csv('members_data.csv', index=False, encoding='utf-8-sig')

print('finished...')

