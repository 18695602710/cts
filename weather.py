# encoding:utf-8
import time,re
from selenium import webdriver
import calendar
####
#p爬取天气预报内容
####
class Weather(object):
    def __init__(self):
        self.day = time.strftime('%d', time.localtime(time.time()))
        self.month = time.strftime('%m', time.localtime(time.time()))

    def get_weather_html(self):
       #打开中国天气网的40天天气预报的网页，爬取数据
       url = 'http://www.weather.com.cn/weather40d/101020100.shtml'
       driver = webdriver.Chrome()
       driver.get(url)
       driver.maximize_window()
       driver.implicitly_wait(3)
       month_input = raw_input('please input month:')
       if month_input != '' and month_input != self.month:
           self.select_month(month_input,driver)
       dict = {}
       for week_index in range(2,8):
           for day_index in range(1,8):
               week = str(week_index)
               day = str(day_index)
               day_path = '//*[@id="table"]/tbody/tr['+week+']/td['+day+']/h2/span[2]'
               max_temp_path = '//*[@id="table"]/tbody/tr['+week+']/td['+day+']/div[1]/p/span[1]'
               min_temp_path = '//*[@id="table"]/tbody/tr['+week+']/td['+day+']/div[1]/p/span[2]'
               date = driver.find_element_by_xpath(day_path)
               date = date.text
               try:
                   date_int = int(date)
               except(ValueError):
                   break
               if month_input == '':
                   month = self.month
               else:
                   month = month_input
               if date_int == 01 and week_index != 2:
                   print u'19年{}月每日温度情况如下'.format(month)
                   break
               max_temp = driver.find_element_by_xpath(max_temp_path)
               min_temp = driver.find_element_by_xpath(min_temp_path)
               max_temp = re.findall('\d+', max_temp.text)
               min_temp = re.findall('\d+', min_temp.text)
               try:
                   max_temp_int = int(max_temp[0])
                   min_temp_int = int(min_temp[0])
               except(IndexError):
                     temp_path = '//*[@id="table"]/tbody/tr['+week+']/td['+day+']/div[2]/h6'
                     temp = driver.find_element_by_xpath(temp_path)
                     max_temp = re.findall('(\d+)/', temp.text)
                     min_temp = re.findall('/(\d+)', temp.text)
                     try:
                         max_temp_int = int(max_temp[0])
                         min_temp_int = int(min_temp[0])
                     except(IndexError):
                         max_temp_path = '//*[@id="table"]/tbody/tr[' + week + ']/td[' + day + ']/div[4]/dl/dt/span[1]/i'
                         min_temp_path = '//*[@id="table"]/tbody/tr[' + week + ']/td[' + day + ']/div[4]/dl/dt/span[2]/i'
                         max_temp = driver.find_element_by_xpath(max_temp_path)
                         min_temp = driver.find_element_by_xpath(min_temp_path)
                         max_temp = re.findall('\d+', max_temp.text)
                         min_temp = re.findall('\d+', min_temp.text)
                         max_temp_int = int(max_temp[0])
                         min_temp_int = int(min_temp[0])
               dict[date_int] = [max_temp_int,min_temp_int]
       return dict,month

    def select_month(self, month, driver):
        driver.find_element_by_xpath('//*[@class="zong"]').click()
        month_path = '//div[@class="w_nian"]/ul[2]/li['+month+']'
        driver.find_element_by_xpath(month_path).click()

if __name__ == '__main__':
    weather = Weather()
    dict,month = weather.get_weather_html()
    count = 0
    for key in dict.keys():
        monthRange = calendar.monthrange(2019, int(month))
        print u"{name:10d}号：{max}~{min}℃".format(name=key,max=dict[key][0],min=dict[key][1])
        count += 1
        if count == monthRange[-1]:
            break