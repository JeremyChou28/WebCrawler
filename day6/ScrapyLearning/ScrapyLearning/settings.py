# Scrapy settings for ScrapyLearning project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# 第一部分：基本配资
# 项目名称，默认的User-Agent由它构成，也作为日志记录的日志名
BOT_NAME = 'ScrapyLearning'
# 爬虫的应用路径
SPIDER_MODULES = ['ScrapyLearning.spiders']
NEWSPIDER_MODULE = 'ScrapyLearning.spiders'

# 客户端的User-Agent请求头
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'ScrapyLearning (+http://www.yourdomain.com)'
# 是否遵循爬虫协议
# Obey robots.txt rules
ROBOTSTXT_OBEY = True
# 并发请求数，线程数
# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# 延迟下载的秒数
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# 单域名访问的并发数，并且延迟下载秒数也应用在每个域名
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# 单IP访问并发数，如果有值则忽略单域名的，并且延迟下载秒数也应用在每个IP
# CONCURRENT_REQUESTS_PER_IP = 16

# 是否支持cookie，cookiejar进行操作cookie
# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Telnet用于查看当前爬虫的信息，操作爬虫等，使用telnet ip port，然后通过命令操作
# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False
# Telnet终端监听的端口
# TELNETCONSOLE_HOST='127.0.0.1'
# Telnet终端使用的端口范围
# TELNETCONSOLE_PORT=[6023 , 6073]

# Scrapy发送http默认的请求头
# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }
# 中间件，pipelines，扩展
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'ScrapyLearning.middlewares.ScrapylearningSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'ScrapyLearning.middlewares.ScrapylearningDownloaderMiddleware': 543,
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# 定义pipeline处理请求
# ITEM_PIPELINES = {
#    'ScrapyLearning.pipelines.ScrapylearningPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# 开启自动限速
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# 初始下载延迟
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# 最大下载延迟
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# 平均每秒并发数
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# 是否显示启用AutoThrottle调试，展示每个接收到的response
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# 是否起用缓存策略
# HTTPCACHE_ENABLED = True
# 缓存超时时间
# HTTPCACHE_EXPIRATION_SECS = 0
# 缓存的保存路径
# HTTPCACHE_DIR = 'httpcache'
# 缓存忽略的http状态码
# HTTPCACHE_IGNORE_HTTP_CODES = []
# 缓存存储的插件
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
