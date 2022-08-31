# @description:基于re模块--爬取糗事百科网的段子信息
# @Author: 周健平
# @company: 山东大学
# @Time: 2020/7/18 10:56
# import scrapy
#
#
# class QiushiSpider(scrapy.Spider):
#     name = 'QiuShi'
#     allowed_domains = ['qiushibaike.com']
#     start_urls = ['http://qiushibaike.com/']
#
#     def parse(self, response):
#         pass
import re
import time

import requests

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

info_lists = []  # 初始化列表，用于装入爬虫信息


def judgementSex(sex):
    # 判断性别
    if sex == 'manIcon':
        return '男'
    else:
        return '女'


def getInfo(url):
    # 爬取信息
    r = requests.get(url, headers=headers)
    user_ids = re.findall('<h2>(.*?)</h2>', r.text, re.S)  # 用户ID
    levels = re.findall('<div class="articleGender \D+Icon">(.*?)</div>', r.text, re.S)  # 用户等级
    sexs = re.findall('<div class="articleGender (.*?)">', r.text, re.S)  # 用户性别
    contents = re.findall('<div class="content">.*?<span>(.*?)</span>', r.text, re.S)  # 笑话内容，
    # 这里需要注意的是，虽然段子信息在<span>标签中，但如果只提取<span>标签会提取到符合规律但不是段子信息的内容，所以需要把匹配的正则写的更详细，加上<div>标签。由于<div>标签与<span>便签之间留有几行空格，所以要通过.*?来匹配出。
    laughs = re.findall('<span class="stats-vote"><i class="number">(\d+)</i>', r.text, re.S)  # 好笑数
    comments = re.findall('<i class="number">(\d+)</i> 评论', r.text, re.S)  # 评论数

    for user_id, level, sex, content, laugh, comment in zip( \
            user_ids, levels, sexs, contents, laughs, comments):
        info = {
            'user_id': user_id,
            'level': level,
            'sex': judgementSex(sex),
            'content': content,
            'laugh': laugh,
            'comment': comment,
        }

        info_lists.append(info)  # 将信息写入字典，添加到列表中
    pass


if __name__ == '__main__':
    urls = ["https://www.qiushibaike.com/text/page/{}/" \
                .format(str(i)) for i in range(1, 14)]
    for url in urls:
        print("正在爬取" + url)
        getInfo(url)
        time.sleep(2)
        for info_list in info_lists:  # 遍历列表，写入文件
            try:
                f = open("qiushibaikeInformation.txt", 'a+', encoding='utf-8')
                f.write(info_list['user_id'] + '\n')
                f.write(info_list['level'] + '\n')
                f.write(info_list['sex'] + '\n')
                f.write(info_list['content'] + '\n')
                f.write(info_list['laugh'] + '\n')
                f.write(info_list['comment'] + '\n')
                f.close()
            except UnicodeEncodeError:  # 此处由于编码问题，在写入content时会出现UnicodeEncodeError，这里暂时先忽略。
                pass
