import random

import requests
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
context = ssl._create_unverified_context()

url='https://github.com/ytdl-org/youtube-dl'
data = {
    'do': 'custom',
    'repository_id': '1039520',
    'thread_types[]': 'Release',
    'authenticity_token': 'H01Dp4JnalalV6SbgAZzfvbWrzOLe0KFA8F8WEp5hF99cO7CZAZhJog6ptEPiVzDmeWsIS3GdqRGZRG7qcRPlg=='

}
header = {
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
        'X-Requested-With':'XMLHttpRequest',
}
proxy = {
    'https': '123.55.102.194:9999'
}
cookie = {
    'Cookie': '_octo=GH1.1.1936862862.1598947318; _ga=GA1.2.1565216233.1598947318; _device_id=72d30595a01d44fc28dc134f2166941d; user_session=y2LMMpRpEJhTlU_3tifIO9TLO3E1Q3x5grPAep3svFjOU_4N; __Host-user_session_same_site=y2LMMpRpEJhTlU_3tifIO9TLO3E1Q3x5grPAep3svFjOU_4N; logged_in=yes; dotcom_user=Francis1998; tz=Asia%2FShanghai; has_recent_activity=1; _gh_sess=Yj9zluSUPfCqSNdGsHUYcPrEwJJ0qJiMoTjzKJgeEOiPK1bKWeAvvNlFxSe17Xw8UxgKfOlAyDOT0HQYTMjOtgMnZNJZWoTYUJmuyVUGNJyhMtDh9r57Xi5NVGaYkV317UsZO5qmLqYoHL3JVapdo6Zj5ZnbQaQ9LkZResELXVV%2FMssrPnwu2P9zB8lop1n8Q5HETAvbAz2DqIWea3nYRvKCputqaWjS37z7XEshlfTcLm9sU5DgHW2ReGcrsHcVmzXeO6YqGKIEW26zOF54HQIdP0dUrdtkkX6MJDPrCjb3C5C777s2D%2BUUNc8g2uKSEjEHErRP3BdLx4Nuidf9aQTK2%2FdPEButkOl7EEKZiDcLihHY4EpvmRnnZp3RwVWuJVGBvKydiAhwO7bLQSBwnNM71i%2B5TWgMD1AS9eu4wlG8Sg1ZTeB5sMAdPjy%2F8e0wSq5KQmd4%2F6ClHxu5nBJRlRwU%2FI6pWl%2B3LCehmYbr%2BnFcHV%2BMfspEEkxMdr%2BaVjp8dSj5PfhI9xxjzGQ5IXuZv5p3JGs%2F1divSwdNUnW4gzGxZh6wcyZXICQfCrPDSf6d7SOYG26Ks%2BOu75kf4mF%2BUyDX2gHaJ0zxphXMpLzBp2KzCmiYon3G%2Ffi5HZtkwPuqlLxZeoWx7nHMT1C2qUvLFbUayay3WtMWfdrseuNyiEEBkhwyHVvZNQvBtv4Wd%2BZ6LanTDQ%3D%3D--myiaaktM3zzgZzc1--UxaER1bCSpwA4%2BsbsjxKqQ%3D%3D',
}
head_connection = ['Keep-Alive','close']
head_accept = ['text/html,application/xhtml+xml,*/*']
head_accept_language = ['zh-CN,fr-FR;q=0.5','en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3']
head_user_agent = ['Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
                       'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.2) Gecko/2008070208 Firefox/3.0.1',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070803 Firefox/1.5.0.12',
                       'Opera/9.27 (Windows NT 5.2; U; zh-cn)',
                       'Mozilla/5.0 (Macintosh; PPC Mac OS X; U; en) Opera 8.0',
                       'Opera/8.0 (Macintosh; PPC Mac OS X; U; en)',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.12) Gecko/20080219 Firefox/2.0.0.12 Navigator/9.0.0.6',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Win64; x64; Trident/4.0)',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Maxthon/4.0.6.2000 Chrome/26.0.1410.43 Safari/537.1 ',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.2; .NET4.0C; .NET4.0E; QQBrowser/7.3.9825.400)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0 ',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.92 Safari/537.1 LBBROWSER',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0; BIDUBrowser 2.x)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/3.0 Safari/536.11']
header = {
        'Connection':head_connection[random.randrange(0,len(head_connection))],
        # 'Accept':head_accept[0],
        # 'Accept-Language':head_accept_language[random.randrange(0,len(head_accept_language))],
        'User-Agent':head_user_agent[random.randrange(0,len(head_user_agent))],
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
        'X-Requested-With':'XMLHttpRequest',
}
r=requests.post(url,data=data,headers=header,verify=False)
print(r.text)