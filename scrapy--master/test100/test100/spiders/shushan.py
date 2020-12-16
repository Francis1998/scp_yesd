# encoding=utf-8
__author__ = 'Shunqi Liu'

import scrapy
from scrapy import Request
from scrapy.spiders import Spider
from test100.items import ShushanItem #需根据自己的项目名称和Item类修改，可不修改
import json
class ShushanSpider(Spider):
    name = "shushan" #爬虫命名，可按照自己要求修改，可不修改
    headers = {
        'Accept': 'application/json',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Content-Length': '547',
        'Content-Type': 'multipart/form-data;boundary=----WebKitFormBoundaryzYfCzX2WMPmnbUwa',
        'Cookie': '_octo=GH1.1.1936862862.1598947318; _ga=GA1.2.1565216233.1598947318; _device_id=72d30595a01d44fc28dc134f2166941d; user_session=y2LMMpRpEJhTlU_3tifIO9TLO3E1Q3x5grPAep3svFjOU_4N; __Host-user_session_same_site=y2LMMpRpEJhTlU_3tifIO9TLO3E1Q3x5grPAep3svFjOU_4N; logged_in=yes; dotcom_user=Francis1998; tz=Asia%2FShanghai; has_recent_activity=1; _gh_sess=Yj9zluSUPfCqSNdGsHUYcPrEwJJ0qJiMoTjzKJgeEOiPK1bKWeAvvNlFxSe17Xw8UxgKfOlAyDOT0HQYTMjOtgMnZNJZWoTYUJmuyVUGNJyhMtDh9r57Xi5NVGaYkV317UsZO5qmLqYoHL3JVapdo6Zj5ZnbQaQ9LkZResELXVV%2FMssrPnwu2P9zB8lop1n8Q5HETAvbAz2DqIWea3nYRvKCputqaWjS37z7XEshlfTcLm9sU5DgHW2ReGcrsHcVmzXeO6YqGKIEW26zOF54HQIdP0dUrdtkkX6MJDPrCjb3C5C777s2D%2BUUNc8g2uKSEjEHErRP3BdLx4Nuidf9aQTK2%2FdPEButkOl7EEKZiDcLihHY4EpvmRnnZp3RwVWuJVGBvKydiAhwO7bLQSBwnNM71i%2B5TWgMD1AS9eu4wlG8Sg1ZTeB5sMAdPjy%2F8e0wSq5KQmd4%2F6ClHxu5nBJRlRwU%2FI6pWl%2B3LCehmYbr%2BnFcHV%2BMfspEEkxMdr%2BaVjp8dSj5PfhI9xxjzGQ5IXuZv5p3JGs%2F1divSwdNUnW4gzGxZh6wcyZXICQfCrPDSf6d7SOYG26Ks%2BOu75kf4mF%2BUyDX2gHaJ0zxphXMpLzBp2KzCmiYon3G%2Ffi5HZtkwPuqlLxZeoWx7nHMT1C2qUvLFbUayay3WtMWfdrseuNyiEEBkhwyHVvZNQvBtv4Wd%2BZ6LanTDQ%3D%3D--myiaaktM3zzgZzc1--UxaER1bCSpwA4%2BsbsjxKqQ%3D%3D',
        'Host': 'github.com',
        'Origin': 'https://github.com',
        'Referer': 'https://github.com/ytdl-org/youtube-dl',
        'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
    } #代理设置，可参考本人设置
    # 发起post：
    # 1.将Request方法中method参数赋值成post
    # 2.FormRequest()可以发起post请求（推荐)
    def start_requests(self):
        formdata = {
            'do': 'custom',
            'repository_id': '1039520',
            'thread_types[]': 'Release',
            'authenticity_token': 'JBzm3zaAVXO9m9F01HHByZr8SCfK9uyyD0ip11c9WwxGIUu60OFeA5D20z5b/u509c9LNWxL2JNK7MQ0tICQxQ=='

        }
        url = 'https://github.com/notifications/subscribe'#访问的初始地址，一般为自己要爬取的网页的第一页地址，必须修改
        temp = json.dumps(formdata)
        yield scrapy.Request(url, body=temp, headers=self.headers,callback=self.parse)
    def parse(self, response):
            with open('D:\\test.txt', 'a', encoding='utf-8') as f:
                f.write(response.body.decode())