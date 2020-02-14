import unittest
import api

from parameterized import parameterized
from api.api_login import Login
from get_log import GetLog
from tools import assert_common, read_data


class Test_Lgoin(unittest.TestCase):

    def setUp(self):
        self.login = Login()
        self.log = GetLog.get_logger()

    @parameterized.expand(read_data("login.yaml"))
    def test_login(self,mobile,password):
        result = self.login.login_inter(mobile,password)
        self.log.info("登录结果：{}".format(result.json()))
        print("登录结果:",result.json())
        assert_common(self,result)
        # 获取 token 值，并追加到信息头
        token = result.json()["data"]
        self.log.info("token值：{}".format(token))
        api.headers["Authorization"] = "Bearer " + token
        print("追加token后的信息头：",api.headers)



