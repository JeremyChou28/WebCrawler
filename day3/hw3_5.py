# @description:百度搜索关键词的提交
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/11 17:01
import urllib.request

url = "https://www.baidu.com/s?wd=python&rsv_spt=1&rsv_iqid=0xfcf2649800010941&issp=1&f=8&rsv_bp=1&rsv_idx=2&ie=utf-8&tn=02003390_5_hao_pg&rsv_enter=1&rsv_dl=tb&rsv_sug3=6&rsv_sug1=5&rsv_sug7=100&rsv_sug2=0&rsv_btype=i&inputT=1443&rsv_sug4=1443"
# headers = ("User-Agent" ,
#            "Mozilla / 5.0( WindowsNT10.0;Win64;x64) AppleWebKit / 537.36( KHTML , likeGecko) Chrome / 83.0.4103.116Safari / 537.36")
# opener = urllib.request.build_opener( )
# opener.addheaders = [headers]
# data = opener.open( url ).read( )
header = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
req = urllib.request.Request(url)
req.add_header('User-Agent', header)
data = urllib.request.urlopen(req).read()

print(data)
