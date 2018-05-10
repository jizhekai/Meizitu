# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import os
from scrapy.utils.project import get_project_settings


class MeizituPipeline(object):
    def process_item(self, item, spider):

        # 从settings里获取存入本地的地址
        IMAGE_STORE = get_project_settings().get("IMAGE_STORE")

        # 创建images文件夹
        if not os.path.exists(IMAGE_STORE + "images"):
            os.mkdir(IMAGE_STORE + "images")

        # 设置保存到本地的图片的名字（该设置为套图入站日期）
        image_path = "-".join(item["image_url"].split(".")[2][4:].split("/"))
        path = IMAGE_STORE + "images" + "\\" + item["title"]

        # 创建每组套图存放的文件夹
        if not os.path.exists(path):
            os.mkdir(path)

        self.filename = open(path + "\\" + image_path + ".jpg", "wb")

        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
            "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            'Cookie': 'Hm_lvt_dbc355aef238b6c32b43eacbbf161c3c=1524481300,1524481926,1524528353,1524546258; Hm_lpvt_dbc355aef238b6c32b43eacbbf161c3c=1524546282',
            'Referer': 'http://i.meizitu.net'
        }

        self.filename.write(requests.get(
            item["image_url"], headers=headers).content)
        return item

    def close_spider(self, spider):
        self.filename.close()
