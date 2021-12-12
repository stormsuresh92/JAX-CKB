from requests_html import HTMLSession
import pandas as pd
import time
from tqdm import tqdm

s = HTMLSession()


data = []
file = open('Input.txt', 'r')
urls = file.readlines()
for url in tqdm(urls):
    try:
        r = s.get(url)
        table = r.html.find('#drugDetailsTable')
        for tdata in table:
            try:
                drugname = tdata.find('#drugDetailsTable > tbody > tr:nth-child(1) > td:nth-child(2)', first=True).text
            except:
                drugname = ''
            try:    
                trade = tdata.find('#drugDetailsTable > tbody > tr:nth-child(2) > td:nth-child(2)', first=True).text
            except:
                trade = ''
            try:
                synonyms = tdata.find('#drugDetailsTable > tbody > tr:nth-child(3) > td.pre-wrap', first=True).text
            except:
                synonyms = ''
            try:    
                desc = tdata.find('#drugDetailsTable > tbody > tr:nth-child(4) > td:nth-child(2) > p', first=True).text
            except:
                desc = ''
            try:    
                drugclass = tdata.find('#drugDetailsTable > tbody > tr:nth-child(5) > td:nth-child(2)', first=True).text
            except:
                drugclass = ''
            try:    
                CAS = tdata.find('#drugDetailsTable > tbody > tr:nth-child(6) > td:nth-child(2)', first=True).text
            except:
                CAS = ''
            try:    
                NCIT = tdata.find('#drugDetailsTable > tbody > tr:nth-child(7) > td:nth-child(2)', first=True).text
            except:
                NCIT = ''
            try:
                url = url
            except:
                url = ''

            dic = {
                'Drug_Name':drugname,
                'Trade_Name':trade,
                'Synonyms':synonyms,
                'Drug_Descriptions':desc,
                'DrugClasses':drugclass,
                'CAS_Registry_Number':CAS,
                'NCIT_ID':NCIT,
                'Urls':url
                }
            data.append(dic)
    except:
        pass



df = pd.DataFrame(data)
df.to_csv('drug_info.csv', index=False)
print('fin')

input()
