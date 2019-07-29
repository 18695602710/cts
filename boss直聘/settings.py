# coding: utf-8

# Scrapy settings for boss project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'boss'

SPIDER_MODULES = ['boss.spiders']
NEWSPIDER_MODULE = 'boss.spiders'

LOG_LEVEL = 'DEBUG'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'boss (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
    "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
    ]

PROXIES = ['https://118.25.40.97:80', 'https://125.123.139.203:9000', 'https://49.82.253.190:8118', 'https://121.232.199.179:9000', 'https://219.131.242.174:9797', 'https://221.216.136.215:9000', 'https://59.78.6.98:1080', 'https://123.172.68.180:53281', 'https://113.119.38.158:3128', 'https://218.94.141.61:21070', 'https://115.213.60.134:53281', 'https://218.94.141.60:21070', 'https://219.137.206.185:53281', 'https://14.115.107.215:808', 'https://117.10.111.80:53281', 'https://42.202.158.49:3128', 'https://115.213.60.133:53281', 'https://119.130.105.113:3128', 'https://114.250.170.119:53281', 'https://114.139.32.232:8118', 'https://218.94.141.59:21070', 'https://120.79.176.70:3128', 'https://59.38.62.2:9797', 'https://163.125.157.163:8888', 'https://58.250.23.210:1080', 'https://218.108.70.86:80', 'https://112.95.205.251:8888', 'https://119.123.247.229:9000', 'https://125.119.31.120:8118', 'https://114.249.115.117:9000', 'https://117.22.42.43:8118', 'https://112.95.21.114:8888', 'https://182.138.229.63:1080', 'https://121.41.20.245:3128', 'https://60.205.57.4:3128', 'https://106.15.176.75:3128', 'https://222.29.32.33:1080', 'https://119.131.89.87:9797', 'https://115.213.63.233:53281', 'https://59.38.60.227:9797', 'https://114.101.41.195:65309', 'https://221.225.147.58:8118', 'https://180.160.139.246:8118', 'https://125.32.80.52:8080', 'https://182.149.157.168:8118', 'https://116.30.120.146:9000', 'https://123.117.34.10:9000', 'https://121.13.252.60:41564', 'https://119.131.89.142:9797', 'https://117.90.1.177:9000', 'http://117.90.5.114:9000', 'https://14.20.235.96:9797', 'https://14.155.112.131:9000', 'https://49.51.86.2:3128', 'https://121.232.148.165:9000', 'https://101.201.199.194:8080', 'https://113.118.159.200:9000', 'https://14.23.58.58:443', 'https://119.254.94.114:45691', 'https://222.189.190.223:9999', 'https://42.238.87.112:9999', 'http://175.165.128.226:1133', 'https://120.83.121.161:9999', 'https://1.198.73.10:9999', 'https://117.91.232.237:9999', 'https://1.197.204.96:9999', 'https://115.219.106.4:8010', 'https://183.6.183.35:8010', 'https://211.159.171.58:80', 'https://113.124.87.62:9999', 'https://1.193.245.123:9999', 'https://1.193.245.87:9999', 'https://221.227.103.121:9999', 'https://122.4.44.59:9999', 'https://171.11.32.161:9999', 'https://114.99.27.97:8010', 'https://60.205.229.126:80', 'https://115.223.106.224:8010', 'https://58.253.153.138:9999', 'https://1.197.204.88:9999', 'https://112.87.69.41:9999', 'https://113.121.22.128:808', 'https://120.83.111.204:9999', 'https://58.253.156.246:9999', 'https://113.121.43.63:9999', 'https://1.198.72.223:9999', 'https://117.91.232.221:9999', 'https://123.163.96.70:9999', 'https://222.189.190.220:9999', 'https://113.121.21.154:9999', 'https://1.197.203.114:9999', 'https://120.83.108.197:9999', 'https://119.120.181.116:9999', 'https://27.43.185.62:9999', 'https://58.253.158.93:9999', 'https://182.35.87.190:9999', 'https://1.198.73.38:9999', 'https://58.253.153.87:9999', 'https://182.34.34.165:9999', 'https://117.91.131.225:9999', 'https://49.86.183.174:9999', 'https://120.83.96.100:9999', 'https://222.189.191.24:9999', 'https://120.83.97.80:9999', 'https://171.13.103.150:9999', 'https://121.233.206.41:9999', 'https://27.43.188.119:9999', 'https://58.253.156.137:9999', 'https://171.13.102.28:9999', 'https://1.198.73.139:9999', 'https://222.189.191.207:9999', 'https://123.163.97.58:9999', 'https://180.119.141.142:9999', 'https://120.83.105.161:9999', 'https://42.238.85.53:9999', 'https://115.53.18.67:9999', 'https://117.91.132.142:9999', 'https://120.83.106.113:9999', 'https://180.119.68.89:9999', 'https://117.91.132.121:9999', 'https://1.197.204.54:9999', 'https://58.253.153.0:9999', 'https://120.83.99.254:9999', 'https://120.83.99.90:9999', 'https://218.91.112.114:9999', 'https://113.120.63.122:9999', 'https://222.95.22.185:3128', 'https://125.116.197.2:1133', 'https://182.35.82.226:9999', 'https://123.52.152.83:9999', 'https://182.35.84.242:9999', 'https://115.221.126.207:9999', 'https://1.197.204.144:9999', 'https://58.253.156.211:9999']


# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 30
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = True

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Connection':'keep-alive'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#     'boss.middlewares.BossSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'boss.middlewares.MyUserAgentMiddleware': 100,
    'boss.middlewares.ProxyMiddleware': 200,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'boss.pipelines.BossPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
