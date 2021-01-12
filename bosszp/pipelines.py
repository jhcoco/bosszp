# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BosszpPipeline:
    def process_item(self, item, spider):
        """
        保存数据到本地 csv 文件
        :param item: 数据项
        :param spider:
        :return:
        """
        with open(file='全国-热门城市岗位数据.csv', mode='a+', encoding='utf8') as f:
            f.write(
                '{job_name},{job_area},{job_salary},{com_name},{com_type},{com_size},{finance_stage},{work_year},'
                '{education},{job_benefits}\n'.format(
                    **item))
        return item
