import time
import unittest
import requests

from Test_iHRM import app
from Test_iHRM.api.empapi import Employee


class TestEmpty(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.employee = Employee()

    def tearDown(self):
        self.session.close()

    def test_add(self):
        respones = self.employee.add(self.session, "圣斗士星矢{}".format(time.strftime("%M%S")),
                                     "14135{}".format(time.strftime("%d%H%M%S")), "95272333")
        self.assertIn("操作成功", respones.json().get("message"))
        print(respones.json())
        id = respones.json().get("data").get("id")
        print(id)
        app.ID = id

    def test_update(self):
        respones1 = self.employee.update(self.session, "雅典娜女神{}".format(time.strftime("%H%M%S")))
        self.assertIn("操作成功", respones1.json().get("message"))
        print(respones1.json())

    def test_get(self):
        respones2 = self.employee.get(self.session)
        self.assertIn("操作成功", respones2.json().get("message"))
        print(respones2.json())

    def test_delete(self):
        respones3 = self.employee.delete(self.session)
        self.assertIn("操作成功", respones3.json().get("message"))
        print(respones3.json().get("message"))
