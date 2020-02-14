import api
import requests

from get_log import GetLog


class Login(object):

    def __init__(self):
        self.url_login = api.host + "/api/sys/login"
        self.log = GetLog.get_logger()

    def login_inter(self,mobile,password):
        data = {"mobile":mobile,"password":password}
        self.log.info("登录信息：{}".format(data))
        self.log.info("登录请求：信息头:{},url{}".format((api.headers),(self.url_login)))
        return requests.post(url=self.url_login,json=data,headers=api.headers)

