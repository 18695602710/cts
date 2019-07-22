# -*- coding: utf-8 -*-
import scrapy
import re
from boss.items import BossItem


class ZhipinSpider(scrapy.Spider):
    name = 'zhipin'
    allowed_domains = ['www.zhipin.com']
    start_urls = ['https://www.zhipin.com/job_detail/?query=python&city=101020100']

    def parse(self, response):
        for page_id in range(1,100):
            print('当前爬取的是第{}页'.format(page_id))
            page = response.xpath('//a[@ka="page-next"]//@href').extract()
            page = re.findall('page=(\d+)', str(page))
            if page != []:
                next_url = 'https://www.zhipin.com/c101020100/?query=python&page=' + str(page[0])
                print('下一次要爬取第{}页'.format(page))
                yield scrapy.Request(url=next_url, callback=self.parse_next)
            else:
                print('爬取完毕')
                break

    def parse_next(self, response):
        job = response.xpath('//*[@class="name"]//@href').extract()
        print(job)
        job = re.findall('/job_detail.*?.html', str(job))
        print(job)
        for i in range(30):
            print('当前在{}项岗位'.format(i))
            job_url = 'https://www.zhipin.com'+job[i]
            yield scrapy.Request(url=job_url, callback=self.parse_job)

    def parse_job(self, response):
        item = BossItem()
        item['job_desc'] = response.xpath('//*[@class="job-sec"]//div[@class="text"]/text()').extract()
        yield item
