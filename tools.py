""" 该本文件内容为公用方法 """


""" 断言的方法 """

def assert_common(self,response,
                  status_code=200,
                  success=True,
                  code=10000,
                  message='操作成功！'):
    """

    :param self: 实例对象
    :param response: 响应数据
    :param status_code:
    :param success:
    :param code:
    :param message:
    :return:
    """

    r = response.json()
    # 断言status_code
    self.assertEqual(status_code, response.status_code)
    # 断言success
    self.assertEqual(success, r["success"])
    # 断言code
    self.assertEqual(code, r["code"])
    # 断言message
    self.assertEqual(message, r['message'])



""" 读取参数化文件的方法 """

import yaml
import config
import os

def read_data(filename):
    with open(config.base_path + os.sep +"data" + os.sep + filename,'r',encoding='utf-8') as f:
        # 以字典形式读取 yaml 文件，需要导入 yaml 包
        # os.sep 自动获取 / 或 \ ，根据操作系统自动识别（os.sep +"data" + os.sep = "/data/"）
        r = yaml.safe_load(f)
        data = []
        for i in r.values():
            data.append(tuple(i.values()))
        return data





