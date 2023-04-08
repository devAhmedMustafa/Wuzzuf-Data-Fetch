from bs4 import BeautifulSoup
import requests
import csv

def fetch_data(data):

    i = 0
    jobs_details = []

    def main(url):

        soup = BeautifulSoup(url.content, 'lxml')
        
        jobs = soup.find('div', {'class':'css-9i2afk'})

        def get_job_details(jobs):

            job_objects = jobs.find_all('div', {'class':'css-1gatmva'})

            for job in job_objects:

                job_details = job.find('div', {'class':'css-laomuu'})
                company_details = job.find('div', {'class':'css-d7j1kk'})
                work_details = job.find('div', {'class':'css-1lh32fc'})

                job_title = job_details.find('h2').text.strip()
                corp_name = company_details.find('a').text.strip()
                job_location = company_details.find('span', {'class':'css-5wys0k'}).text.strip()
                work_time = work_details.find_all('a')[0].find('span').text.strip()

                details = {
                    'Job Category': data,
                    'Job Title': job_title,
                    'Corp': corp_name,
                    'Job Location': job_location,
                    'Work Time': work_time,
                }

                jobs_details.append(details)

        get_job_details(jobs)

    b = True

    while b == True:
        length = len(jobs_details)
        url = requests.get(f"https://wuzzuf.net/a/{data}-in-Egypt?ref=browse-jobs&start={i}") # type: ignore
        main(url)
        i = i +1
        if len(jobs_details) == length:
            b = False
    
    return jobs_details



def write_csv(jobs_details):

    keys = jobs_details[0].keys()

    with open('media/files/wuzzuf.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        writer.writerows(jobs_details)
        print(csvfile)