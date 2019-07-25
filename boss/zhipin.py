# -*- coding: utf-8 -*-
import scrapy
import re
from boss.items import BossItem


class ZhipinSpider(scrapy.Spider):
    name = 'zhipin'
    allowed_domains = ['www.zhipin.com']
    start_urls = ['https://www.zhipin.com/c101020100/?query=python&page=1',
                  'https://www.zhipin.com/c101020100/?query=python&page=2',
                  'https://www.zhipin.com/c101020100/?query=python&page=3',
                  'https://www.zhipin.com/c101020100/?query=python&page=4',
                  'https://www.zhipin.com/c101020100/?query=python&page=5',
                  'https://www.zhipin.com/c101020100/?query=python&page=6',
                  'https://www.zhipin.com/c101020100/?query=python&page=7',
                  'https://www.zhipin.com/c101020100/?query=python&page=8',
                  'https://www.zhipin.com/c101020100/?query=python&page=9',
                  'https://www.zhipin.com/c101020100/?query=python&page=10']

    # def start_requests(self):
    #     for i in self.start_urls:
    #         yield scrapy.Request(i, meta={
    #             'dont_redirect': True,
    #             'handle_httpstatus_list': [302]
    #         }, callback=self.parse)

    def parse(self, response):
        job = response.xpath('//*[@class="name"]//@href').extract()
        job = re.findall('/job_detail.*?.html', str(job))
        print('job:{}'.format(job))
        for i in range(1):
            print('当前在{}项岗位'.format(i))
            job_url = 'https://www.zhipin.com'+job[i]
            yield scrapy.Request(url=job_url, callback=self.parse_job)

    def parse_job(self, response):
        item = BossItem()
        item['job_desc'] = response.xpath('//*[@class="job-sec"]//div[@class="text"]/text()').extract()
        yield item
