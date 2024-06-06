from bs4 import BeautifulSoup
import requests
import time

# with open('home.html', 'r') as html_file:
#     content = html_file.read()
#
#     soup = BeautifulSoup(content, 'lxml')
#     tags = soup.find('head')
#     print(tags)

def find_job():
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=java&txtLocation=').text
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ ='clearfix job-bx wht-shd-bx')

    for job in jobs:
        published_date = job.find('span', class_ ='sim-posted').span.text

        if 'few' in published_date:
            company_name = job.find('h3', class_ ='joblist-comp-name').text.replace(' ', '')
            skills = job.find('span', class_ ='srp-skills').text.replace(' ', '')
            more_info = job.header.h2.a['href']
            print(f"Company Name : {company_name.strip()}")
            print(f"Required Skills: {skills.strip()}")
            print(f"More Info: {more_info}")

            print()

if __name__ == '__main__':
    while True:
        find_job()
        time_wt = 1
        print(f"Waiting {time_wt} minute(s)...")
        time.sleep(time_wt * 60)
