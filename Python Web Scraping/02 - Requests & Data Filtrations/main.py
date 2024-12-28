from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
soup = BeautifulSoup(html_text, 'lxml')
jobs = soup.find_all('li', class_= 'clearfix job-bx wht-shd-bx')

for job in jobs:

    published_date = job.find('span', class_ = 'sim-posted').span.text

    if 'few' in published_date:
        company_name = job.find('h3', class_ = 'joblist-comp-name').text.replace('\t', '').replace(' ', ''). replace('\n', '')
        skills = job.find('div', class_ = 'srp-skills').text.replace('\t', '').replace(' ', '').replace('\n\n', '').replace('\n', ' ')
    
        print(f'''
Company Name: {company_name}
Required Skills: {skills}
        ''')

        print('')
