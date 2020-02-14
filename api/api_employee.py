import api
import requests

from get_log import GetLog


class Employee(object):

    def __init__(self):
        # 获取日志器
        self.log = GetLog.get_logger()
        # 新增员工 url
        self.add_url = api.host + "/api/sys/user"
        # 修改员工 url
        self.update_url = api.host + "/api/sys/user/{}"
        # 查询员工 url
        self.search_url = api.host + "/api/sys/user/{}"
        # 删除员工 url
        self.delete_url = api.host + "/api/sys/user/{}"

    # 新增员工的方法
    def add_employee(self,username,mobile,workNumber):
        data = {"username": username,"mobile": mobile,"workNumber": workNumber}
        # 标记日志
        self.log.info("新增员工信息数据：{}".format(data))
        self.log.info("新增员工请求：信息头:{},url:{}".format((api.headers),(self.add_url)))
        return requests.post(url=self.add_url,headers=api.headers,json=data)

    # 修改员工的方法
    def update_employee(self,username):
        data = {"username": username}
        # 标记日志
        self.log.info("修改员工信息：{}".format(data))
        self.log.info("修改员工请求：信息头:{},url:{}".format((api.headers), (self.update_url.format(api.user_id))))
        return requests.put(url=self.update_url.format(api.user_id),headers=api.headers,json=data)

    # 查询员工的方法
    def search_employee(self):
        self.log.info("查询员工请求：信息头:{},url:{}".format((api.headers), (self.search_url.format(api.user_id))))
        return requests.get(url=self.search_url.format(api.user_id),headers=api.headers)

    # 删除员工的方法
    def delete_employee(self):
        self.log.info("删除员工请求：信息头:{},url:{}".format((api.headers), (self.delete_url.format(api.user_id))))
        return requests.delete(url=self.delete_url.format(api.user_id),headers=api.headers)