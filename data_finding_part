import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

#Возьмем информацию Freedom House о степени политической свободы в разных странах 
url_1 = 'https://freedomhouse.org/countries/freedom-world/scores'
response = requests.get(url_1)
page = BeautifulSoup(response.text, 'html')
results = page.body.table.findAll(['tr','span'])
my_list = []
for result in results:
    my_list.append(result.text.strip())
new_list = my_list[3:]
list_1 = []
for x in new_list:
    list_2 = [x.split('\n')]
    list_1.append(list_2[0])
for i in list_1:
    if len(i[0])<=3:
        del list_1[list_1.index(i)]
first_list = []
second_list = []
for ind in range(0,len(list_1)):
    if ind % 2 == 0:
        first_list.append(list_1[ind][0])
    else:
        second_list.append(list_1[ind][0])
for index, z in enumerate(first_list):
    if '*'in z:
        a = [z.split('*')][0]
        first_list[index] = a[0]
my_dict = {'Country': first_list,
'Political Freedom': second_list}
df = pd.DataFrame(my_dict)
#С помощью JSON и Википедии получим список центральных банков стран
url = "https://en.wikipedia.org/w/api.php"
params = {'action': 'query',
    'list': 'categorymembers',
    'cmtitle': "Category:Central banks",
    'format': 'json'}
###FROM: Lesson21(https://gist.github.com/ischurov/8ca2f7b2939768a5b83ef53e6c349beb)
titles = []
while True:
    r = requests.get(url, params=params)
    data = r.json()
    titles.extend([cm['title'] for cm in data['query']['categorymembers']])
    if 'continue' not in data:
        break
    params.update(data['continue'])
###END FROM
#Из полученного списка удалим статьи, которые не относятся к центральным банкам отдельных стран
new_titles = titles[6:-14]
new_titles.remove('Bank for International Settlements')
new_titles.remove('Royal Monetary Authority of Bhutan')
new_titles.remove('Central Liquidity Facility')
new_titles.remove('Basel Committee on Banking Supervision')
new_titles.remove('Commonwealth banknote-issuing institutions')
new_titles.remove('European DataWarehouse')
new_titles.remove('Financial Stability Board')
new_titles.remove('Flow of funds')
new_titles.remove('African Central Bank')
new_titles.remove('Fractional-reserve banking')
new_titles.remove('History of central banking in the United States')
new_titles.remove("Institut d'émission d'outre-mer")
new_titles.remove('Monetary authority')
new_titles.remove('Nominal income target')
new_titles.remove('National Bank Building, Belgrade')
new_titles.remove('Governor of the Eastern Caribbean Central Bank')
#Сначала получим названия стран, которые явно указаны в названиях банков
k = []
m_list = []
for elem in new_titles:
    m_list.append(elem.split(' of '))
    for b in m_list:
                if len(b)>1:
                    k.append(b[1])
final_list = []
for eleme in k:
    if eleme not in final_list:
        final_list.append(eleme)
#Заменим некоторые названия так, чтобы они совпадали с данными из первого датафрейма
final_list[12]='Belarus'
final_list[22]='Cabo Verde'
final_list[24]='Central African Republic'
final_list[27]='Colombia'
final_list[28]='Comoros'
final_list[29]='Democratic Republic of the Congo'
final_list[35]='Dominican Republic'
final_list[39]='United Kingdom'
final_list[65]='North Korea'
final_list[66]='South Korea'
final_list[69]='Kyrgyzstan'
final_list[70]='Laos'
final_list[96]='Northern Cyprus'
final_list[131]='United Arab Emirates'
#Можно проверить, что таких банков будет 142 из 180. Добавим оставшиеся страны
final_list.insert(0,'Afghanistan')
final_list.insert(3,'Andorra')
final_list.insert(9,'Austria')
final_list.insert(13,'Timor-Leste')
final_list.insert(14,'Bangladesh')
final_list.insert(20,'Bermuda')
final_list.insert(26,'Brunei')
final_list.insert(27,'Bulgaria')
final_list.insert(28,'Burundi')
final_list.insert(33,'Cayman Islands')
final_list.insert(37,'Taiwan')
final_list.insert(42,'Croatia')
final_list.insert(46,'Denmark')
final_list.insert(49,'Eastern Caribbean')
final_list.insert(63,'Germany')
final_list.insert(66,'Guinea')
final_list.insert(68,'Haiti')
final_list.insert(70,'Hong Kong')
final_list.insert(71,'Hungary')
final_list.insert(74,'Indonesia')
final_list.insert(92,'Lebanon')
final_list.insert(103,'Maldives')
final_list.insert(111,'Al-Maghrib')
final_list.insert(116,'Nepal')
final_list.insert(117,'Netherlands')
final_list.insert(122,'Norway')
final_list.insert(125,'Palestine')
final_list.insert(130,'Philippines')
final_list.insert(132,'Portugal')
final_list.insert(133,'Qatar')
final_list.insert(138,'Saudi Arabia')
final_list.insert(141,'Shinkin')
final_list.insert(149,'South Africa')
final_list.insert(155,'Sweden')
final_list.insert(156,'Switzerland')
final_list.insert(162,'Transnistria')
final_list.insert(165,'Turkey')
final_list.insert(169,'United States')
new_dict = {'Country': final_list,
'Central bank': new_titles}
df_1 = pd.DataFrame(new_dict)
#С помощью Selenium соберем список стран и регионов, к которым относятся эти страны
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")
url1 = "https://www.who.int/countries"
driver.get(url1)
parts = driver.find_elements(By.CSS_SELECTOR, "div.sf-publications-item__header")
regions = [] 
for part in parts:
    region = part.find_element(By.CSS_SELECTOR, "div.sf-publications-item__date").text
    regions.append(region)
parts_1 = driver.find_elements(By.CSS_SELECTOR, "div.sf-publications-item__header")
countries = []
for part_1 in parts_1:
    country = part_1.find_element(By.CSS_SELECTOR, "h3.sf-publications-item__title").text
    countries.append(country)
countries[20]='Bolivia'
countries[24]='Brunei'
countries[46]='North Korea'
countries[80]='Iran'
countries[93]='Laos'
countries[111]='Micronesia'
countries[140]='South Korea'
countries[141]='Moldova'
countries[143]='Russia'
countries[145]='St. Kitts and Nevis'
countries[146]='St. Lucia'
countries[147]='St. Vincent and the Grenadines'
countries[169]='Syria'
countries[183]='United Kingdom'
countries[184]='Tanzania'
countries[185]='United States'
countries[189]='Venezuela'
countries[190]='Vietnam'
c_dict = {'Country': countries,
'Region': regions}
c_df = pd.DataFrame(c_dict)
url2 = "https://ourworldindata.org/grapher/gross-domestic-product?tab=table"
driver.get(url2)
v=driver.find_elements(by=By.XPATH, value="//table[@class='data-table']/tbody/tr/td[1]")
countr = []
for w in v:
    countr.append(w.text)
countr[5]='Samoa'
countr[37]='Cabo Verde'
countr[53]='Czech Republic'
countr[54]='Democratic Republic of the Congo'
countr[151]='Micronesia'
m = driver.find_elements(by=By.XPATH, value="//table[@class='data-table']/tbody/tr/td[3]")
gdps = []
for l in m:
    gdps.append(l.text)
gdps[5]='$522,466,367.71'
gdps[12]='$2,805,918,209.61'
gdps[24]='$6,025,347,991.58'
gdps[51]='$77,122,848,823.24'
gdps[56]='$1,128,611,700.36'
gdps[67]='$1,727,482,210.55'
gdps[87]='$2,762,593,126.01'
gdps[111]='$7,946,530,864.97'
gdps[115]='$6,187,013,947,904.92'
gdps[147]='$187,517,718.07'
gdps[157]='$8,152,851,305.85'
gdps[173]='$941,000,000.00'
gdps[176]='$75,032,818,560.74'
gdps[180]='$217,497,809.81'
gdps[200]='$1,723,484,312.19'
gdps[216]='$7,832,417,790.54'
gdps[231]='$455,079,252.29'
gdps[235]='$47,566,453,010.86'
gdps[240]='$404,700,030,660.31'
gdps[248]='$421,393,747,431.43'
gdps[251]='$18,037,064,825.94'
g_dict = {'Country': countr,'Annual GDP(2020)': gdps}
gd_df = pd.DataFrame(g_dict)
url3 = "https://ourworldindata.org/grapher/gdp-per-capita-worldbank?tab=table"
driver.get(url3)
t=driver.find_elements(by=By.XPATH, value="//table[@class='data-table']/tbody/tr/td[1]")
count = []
for e in t:
    count.append(e.text)
count[11]='The Bahamas'
count[32]='Cabo Verde'
count[46]='Czech Republic'
count[47]='Democratic Republic of the Congo'
f = driver.find_elements(by=By.XPATH, value="//table[@class='data-table']/tbody/tr/td[3]")
gpc = []
for d in f:
    gpc.append(d.text)
gpc[7]='$38,897'
gpc[193]='$15,538'
gc_dict = {'Country': count,'GDP per capita (2020)': gpc}
gc_df = pd.DataFrame(gc_dict)
url4 = "https://ourworldindata.org/grapher/growth-rate-of-real-gdp-per-employed-person?tab=table"
driver.get(url4)
j = driver.find_elements(by=By.XPATH, value="//table[@class='data-table']/tbody/tr/td[1]")
cou = []
for c in j:
    cou.append(c.text)
cou[13]= 'The Bahamas'
cou[33]= 'Cabo Verde'
cou[44]= 'Hong Kong'
cou[53]='Czech Republic'
cou[54]='Democratic Republic of the Congo'
u = driver.find_elements(by=By.XPATH, value="//table[@class='data-table']/tbody/tr/td[3]")
grow = []
for s in u:
    grow.append(s.text)
grow_dict = {'Country': cou,'Growth rate of GDP per employed person(2021)': grow}
grow_df = pd.DataFrame(grow_dict)
url5 = "https://ourworldindata.org/grapher/population-by-income-level?tab=table"
driver.get(url5)
st = driver.find_elements(by=By.XPATH, value="//table[@class='data-table']/tbody/tr/td[1]")
states = []
for state in st:
    states.append(state.text)
states[13]='The Bahamas'
states[35]='Cabo Verde'
states[51]='Czech Republic'
states[52]='Democratic Republic of the Congo'
pop = driver.find_elements(by=By.XPATH, value="//table[@class='data-table']/tbody/tr/td[3]")
population = []
for person in pop:
    population.append(person.text)
p_dict = {'Country': states,'Population(2020)': population}
p_df = pd.DataFrame(p_dict)
df1 = pd.merge(c_df,p_df, how='inner')
df2 = pd.merge(df1, df, how="inner") 
df3 = pd.merge(df2, df_1, how='inner')
df4 = pd.merge(df3, gd_df, how='inner')
df5 = pd.merge(df4, gc_df,how='inner')
df6 = pd.merge(df5,  m_df, how='inner')
df7 = pd.merge(df6, fi_df, how='inner')
first_df = pd.merge(df7, u_df, how='inner')
first_df
