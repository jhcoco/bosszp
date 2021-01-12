# -*- coding:utf-8 -*-
"""
    作者：jhzhong
    功能：连接数据库，封装了操作数据库的增删改查等常见操作函数
"""

import pymysql
import logging


class DBUtils(object):
    # 初始化连接对象和游标对象
    _db_conn = None
    _db_cursor = None

    """
        数据库工具类 初始化方法
        传入 host，user，password，db 进行数据库连接
    """

    def __init__(self, host, user, password, db, port=3306, charset='utf8'):
        try:
            self._db_conn = pymysql.connect(host=host, user=user, password=password, port=port, db=db, charset=charset)
            self._db_cursor = self._db_conn.cursor()
        except Exception as e:
            logging.error(e)

    def get_one(self, sql_str, args=None):
        """
        查询单个结果，返回具体的数据内容
        :param sql_str: sql语句
        :param args: 参数列表
        :return: result
        """
        try:
            if self._db_conn is not None:
                self._db_cursor.execute(sql_str, args=args)
                result = self._db_cursor.fetchone()
                return result
            else:
                logging.error("请检查数据库连接")
        except Exception as e:
            logging.error(e)

    # 查询多个结果
    def get_all(self, sql_str, args=None):
        """
        查询多个结果，返回元组对象
        :param sql_str: sql 语句
        :param args: 参数列表
        :return: result
        """
        try:
            if self._db_conn is not None:
                self._db_cursor.execute(sql_str, args=args)
                result = self._db_cursor.fetchall()
                return result
            else:
                logging.error("请检查数据库连接")
        except Exception as e:
            logging.error(e)

    # 插入数据
    def insert(self, sql_str, args=None):
        """
        向数据库插入数据，返回影响行数（int）
        :param sql_str: sql 语句
        :param args: 参数列表
        :return: affect_rows
        """
        try:
            if self._db_conn is not None:
                affect_rows = self._db_cursor.execute(sql_str, args=args)
                self._db_conn.commit()
                return affect_rows
            else:
                logging.error("请检查数据库连接")
        except Exception as e:
            self._db_conn.rollback()
            logging.error(e)

    # 修改数据
    def modify(self, sql_str, args=None):
        """
        更新数据，返回影响行数（int）
        :param sql_str: sql 语句
        :param args: 参数列表
        :return: affect_rows
        """
        return self.insert(sql_str=sql_str, args=args)

    # 删除数据
    def delete(self, sql_str, args=None):
        """
        删除数据，返回影响行数（int）
        :param sql_str: sql 语句
        :param args: 参数列表
        :return: affect_rows
        """
        return self.insert(sql_str=sql_str, args=args)

    def __del__(self):
        """
        程序运行结束后，会默认调用 __del__ 方法
        销毁对象
        """
        if self._db_conn is not None:
            self._db_cursor.close()
            self._db_conn.close()
