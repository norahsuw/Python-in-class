import requests
import bs4
import random
import time
import csv
def job_list(url): 
    global company_job
    global n
    htmlFile = requests.get(url) 
    objSoup = bs4.BeautifulSoup(htmlFile.text,'lxml')
    jobs = objSoup.find_all('article', class_='js-job-item') 
    for job in jobs: 
        cop_name=job.get('data-cust-name')
        job_name=job.get('data-job-name')
        dict1={"編號":n,"公司名稱":cop_name,"職務名稱":job_name}
        print("公司名稱:" , cop_name)
        print("職務名稱:" , job_name)
        company_job.append(dict1)
        n=n+1

def write_to_csv(): 
    f_name="104_job.csv" 
    with open(f_name,"w",newline="") as csvFile:
        fields=["編號","公司名稱","職務名稱"]
        dictWriter=csv.DictWriter(csvFile,fieldnames=fields)
        dictWriter.writeheader()
        for row in company_job: 
            dictWriter.writerow(row)

def main():
    p=1
    urls = ['https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=Python&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=14&asc=0&page=12&mode=s&jobsource=2018indexpoc',
            'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=Python&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=14&asc=0&page=2&mode=s&jobsource=2018indexpoc',
            'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=Python&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=14&asc=0&page=3&mode=s&jobsource=2018indexpoc',
            'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=Python&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=14&asc=0&page=4&mode=s&jobsource=2018indexpoc',
            'https://www.104.com.tw/jobs/search/?ro=0&kwop=7&keyword=Python&expansionType=area%2Cspec%2Ccom%2Cjob%2Cwf%2Cwktm&order=14&asc=0&page=5&mode=s&jobsource=2018indexpoc']
    for url in urls:
        print('-'*50)
        print(' page '+str(p))
        print('-'*50)
        job_list(url) 
        time.sleep(random.randint(3,5)) 
        p=p+1
    write_to_csv()
n=1
company_job=[]
main()
