# -*- coding: utf-8 -*-
import scrapy,json,time,random


class WechatSpider(scrapy.Spider):
    name = 'wechat'
    allowed_domains = ['weixin.qq.com']
    start_urls = ['https://mp.weixin.qq.com/cgi-bin/appmsg?token=1852289620&action=list_ex&begin={}&count=5&query=&fakeid=MzI2OTA3MTA5Mg%3D%3D&type=9']
    begin = 0

    def start_requests(self):
        yield scrapy.Request(self.start_urls[0].format("0"),callback=self.parse)

    def parse(self, response):
        html = json.loads(response.body_as_unicode())
        app_msg_list = html["app_msg_list"]
        app_msg_cnt = html["app_msg_cnt"]
        for item in app_msg_list:
            yield item


        print(app_msg_cnt,self.begin)
        if app_msg_cnt > self.begin:
            self.begin += 5
            time.sleep(random.randint(5,9))
            yield scrapy.Request(self.start_urls[0].format(self.begin),callback=self.parse)