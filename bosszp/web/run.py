# -*- coding:utf-8 -*-
"""
    作者：jhzhong
    功能：数据分析于可视化
"""

from flask import Flask, render_template
from bosszp.web.dbutils import DBUtils
import json

app = Flask(__name__)


def get_db_conn():
    """
    获取数据库连接
    :return: db_conn 数据库连接对象
    """
    return DBUtils(host='localhost', user='root', password='123456', db='bosszp_db')


def msg(status, data='未加载到数据'):
    """
    :param status: 状态码 200成功，201未找到数据
    :param data: 响应数据
    :return: 字典 如{'status': 201, 'data': ‘未加载到数据’}
    """
    return json.dumps({'status': status, 'data': data})


@app.route('/')
def index():
    """
    首页
    :return: index.html 跳转到首页
    """
    return render_template('index.html')


@app.route('/getwordcloud')
def get_word_cloud():
    """
    获取岗位福利词云数据
    :return:
    """
    db_conn = get_db_conn()
    text = \
        db_conn.get_one(sql_str="SELECT GROUP_CONCAT(job_benefits) FROM t_boss_zp_info")[0]
    if text is None:
        return msg(201)
    return msg(200, text)


@app.route('/getjobinfo')
def get_job_info():
    """
    获取热门岗位招聘区域分布
    :return:
    """
    db_conn = get_db_conn()
    results = db_conn.get_all(
        sql_str="SELECT city,district,COUNT(1) as num FROM t_boss_zp_info GROUP BY city,district")
    # {"city":"北京","info":[{"district":"朝阳区","num":27},{"海淀区":43}]}

    if results is None or len(results) == 0:
        return msg(201)
    data = []
    city_detail = {}
    for r in results:
        info = {'name': r[1], 'value': r[2]}
        if r[0] not in city_detail:
            city_detail[r[0]] = [info]
        else:
            city_detail[r[0]].append(info)
    for k, v in city_detail.items():
        temp = {'name': k, 'data': v}
        data.append(temp)
    return msg(200, data)


@app.route('/getjobnum')
def get_job_num():
    """
    获取个城市岗位数量
    :return:
    """
    db_conn = get_db_conn()
    results = db_conn.get_all(sql_str="SELECT city,COUNT(1) num FROM t_boss_zp_info GROUP BY city")
    if results is None or len(results) == 0:
        return msg(201)
    if results is None or len(results) == 0:
        return msg(201)
    data = []
    for r in results:
        data.append(list(r))
    return msg(200, data)


@app.route('/getcomtypenum')
def get_com_type_num():
    """
    获取企业类型占比
    :return:
    """
    db_conn = get_db_conn()
    results = db_conn.get_all(
        sql_str="SELECT com_type, ROUND(COUNT(1)/(SELECT SUM(t1.num) FROM (SELECT COUNT(1) num FROM t_boss_zp_info GROUP BY com_type) t1)*100,2) percent FROM t_boss_zp_info GROUP BY com_type")
    if results is None or len(results) == 0:
        return msg(201)
    data = []
    for r in results:
        data.append({'name': r[0], 'y': float(r[1])})
    return msg(200, data)


# 扇形图
@app.route('/geteducationnum')
def geteducationnum():
    """
    获取学历占比
    :return:
    """
    db_conn = get_db_conn()
    results = db_conn.get_all(
        sql_str="SELECT t1.education,ROUND(t1.num/(SELECT SUM(t2.num) FROM(SELECT COUNT(1) num FROM t_boss_zp_info t GROUP BY t.education)t2)*100,2) FROM( SELECT t.education,COUNT(1) num FROM t_boss_zp_info t GROUP BY t.education) t1")
    if results is None or len(results) == 0:
        return msg(201)
    data = []
    for r in results:
        data.append([r[0], float(r[1])])
    return msg(200, data)


# 获取排行榜
@app.route('/getorder')
def getorder():
    """
    获取企业招聘数量排行榜
    :return:
    """
    db_conn = get_db_conn()
    results = db_conn.get_all(
        sql_str="SELECT t.com_name,COUNT(1) FROM t_boss_zp_info t GROUP BY t.com_name ORDER BY COUNT(1) DESC LIMIT 10")
    if results is None or len(results) == 0:
        return msg(201)
    data = []
    for i, r in enumerate(results):
        data.append({'id': i + 1,
                     'name': r[0],
                     'num': r[1]})
    return msg(200, data)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
