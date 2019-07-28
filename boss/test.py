# import telnetlib
# try:
#   telnetlib.Telnet('180.168.13.26', port='8000', timeout=10)
# except:
#   print('connect failed')
# else:
#   print('success')
import requests,re
from bs4 import BeautifulSoup
ip_list = ['http://120.132.53.21:8888','http://47.106.216.42:8000','http://117.191.11.80:8080',
           'http://117.191.11.76:80','http://117.191.11.113:8080','http://27.208.90.212:8060',
           'http://116.114.19.211:443','http://116.196.90.176:3128','http://183.57.36.87:8888',
           'http://117.191.11.111:8080','http://60.217.73.238:8060','http://112.84.178.21:8888',
           'http://112.247.177.90:8060','http://112.247.177.164:8060','http://112.80.41.78:8888',
           'http://112.35.56.134:80','http://112.80.41.86:8888','http://180.150.191.150:8888',
           'http://120.234.63.196:3128','http://60.205.188.24:3128','http://120.132.52.248:8888',
           'http://120.132.52.79:8888','http://180.175.16.227:8060','http://27.208.89.118:8060',
           'http://183.146.213.157:80','http://60.217.138.187:8060','http://123.139.56.238:9999',
           'http://1.197.16.197:9999','http://36.25.243.251:80','http://39.137.69.6:8080',
           'http://1.197.16.160:9999','http://120.132.52.137:8888','http://111.231.140.109:8888',
           'http://117.191.11.110:8080','http://27.208.64.4:8060','http://39.137.107.98:80']
success_list = []
url = 'http://ip.chinaz.com/'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
}
for i in ip_list:
    print('i:{}'.format(i))
    protocol = re.findall('(\w+)://',i)
    proxies = {protocol[0]:i}
    print('proxies is {}'.format(proxies))
    # r = requests.get(url, headers=headers, proxies=proxies)
    # soup = BeautifulSoup(r.text, 'lxml')
    # parent_node = soup.find(class_="IpMRig-tit")
    # for i in parent_node.find_all('dd'):
    #     print(i.get_text())
    try:
        response = requests.get('http://ip.chinaz.com/', headers=headers,  proxies=proxies, timeout=5)
        soup = BeautifulSoup(response.text, 'lxml')
        parent_node = soup.find(class_="IpMRig-tit")
        for i in parent_node.find_all('dd'):
             print(i.get_text())
    except:
        print('connect failed')
    else:
        print('success')
        success_list.append(i)
print(success_list)

