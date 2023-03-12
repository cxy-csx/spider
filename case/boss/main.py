import csv
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver_path = r'D:\software\chromedriver.exe'
driver = webdriver.Chrome(executable_path=driver_path)


def get_post_data(url):
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)

    jobs = []

    lis = driver.find_elements(By.CLASS_NAME, "job-card-wrapper")
    for item in lis:
        job_name = item.find_element(By.CLASS_NAME, 'job-name').text
        job_area = item.find_element(By.CLASS_NAME, 'job-area').text
        job_salary = item.find_element(By.CLASS_NAME, 'salary').text
        job_tags = item.find_element(By.CLASS_NAME, 'tag-list').text
        job_company = item.find_element(By.CLASS_NAME, 'company-name').text
        job_company_tags = item.find_element(By.CLASS_NAME, 'company-tag-list').text
        job_info = item.find_element(By.CLASS_NAME, 'info-desc').text
        job_url = item.find_element(By.CLASS_NAME, 'job-card-body').find_element(By.TAG_NAME, 'a').get_attribute('href')
        print(job_url)
        jobs.append(
            (job_company, job_name, job_area, job_salary, job_company_tags, job_tags, job_info, job_url)
        )

    return jobs


def main():
    all_job = []
    url = 'https://www.zhipin.com/web/geek/job?query=前端开发工程师&city=101280600&page={}'
    for page in range(1, 11):
        page_url = url.format(page)
        print(page_url)
        jobs = get_post_data(page_url)
        if not jobs:
            jobs = get_post_data(page_url)
        print(jobs)
        all_job += jobs
        time.sleep(3)

    with open('boss.csv', 'w', newline='') as fp:
        headers = ['公司', '职位', '地区', '薪资', '公司标签', '经验', '工作福利', '链接']
        writer = csv.writer(fp)
        writer.writerow(headers)
        writer.writerows(all_job)


if __name__ == '__main__':
    main()
