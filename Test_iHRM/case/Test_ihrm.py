import json
import unittest

import requests

from Test_iHRM import app
from Test_iHRM.api.Admin_api import AdminLogin

from parameterized import parameterized


def read_json():
    data = []
    with open(app.Pro_Path + "/data/data_login.json", "r", encoding="utf-8") as f:
        for value in json.load(f).values():
            mobile = value.get("mobile")
            password = value.get("password")
            success = value.get("success")
            code = value.get("code")
            message = value.get("message")
            elp = (mobile, password, success, code, message)
            data.append(elp)
        return data


class TestIhrm(unittest.TestCase):
    def setUp(self):
        self.session = requests.Session()
        self.admin_login = AdminLogin()

    def tearDown(self):
        self.session.close()

    @parameterized.expand(read_json())
    def test_login(self, mobile, password, success, code, message):
        response1 = self.admin_login.post_login(self.session, mobile, password)
        print(response1.json())
        self.assertEqual(success, response1.json().get("success"))
        self.assertEqual(code, response1.json().get("code"))
        self.assertEqual(message, response1.json().get("message"))

    def test_login_success(self):
        response = self.admin_login.post_login(self.session, "13800000002", "123456")
        msg = response.json()
        self.assertEqual(True, msg.get("success"))
        self.assertEqual(10000, msg.get("code"))
        self.assertIn("操作成功", msg.get("message"))
        print(msg)
        token = msg.get("data")
        app.Token = token
