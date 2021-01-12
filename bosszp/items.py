# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BosszpItem(scrapy.Item):
    job_name = scrapy.Field()  # 岗位名
    job_area = scrapy.Field()  # 工作地址
    job_salary = scrapy.Field()  # 薪资
    com_name = scrapy.Field()  # 企业名称
    com_type = scrapy.Field()  # 企业类型
    com_size = scrapy.Field()  # 企业规模
    finance_stage = scrapy.Field()  # 融资情况
    work_year = scrapy.Field()  # 工作年限
    education = scrapy.Field()  # 学历要求
    job_benefits = scrapy.Field()  # 岗位福利
