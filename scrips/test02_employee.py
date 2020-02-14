import unittest
import api
from api.api_employee import Employee
from get_log import GetLog
from tools import assert_common


class Test_Employee(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.employee = Employee()
        self.log = GetLog.get_logger()

    def test_01_add(self):
        r = self.employee.add_employee("xixixi","14900000000","478295")
        self.log.info("新增员工返回结果：{}".format(r.json()))
        # 获取 ID 值
        id = r.json().get("data").get("id")
        self.log.info("ID值：{}".format(id))
        api.user_id = id
        assert_common(self,r)

    def test_02_update(self):
        e = self.employee.update_employee("xixixi-new")
        self.log.info("更新员工返回结果：{}".format(e.json()))
        assert_common(self,e)


    def test_03_search(self):
        a = self.employee.search_employee()
        self.log.info("查询员工返回结果：{}".format(a.json()))
        assert_common(self,a)

    def test_04_delete(self):
        b = self.employee.delete_employee()
        self.log.info("删除员工返回结果：{}".format(b.json()))
        assert_common(self,b)
