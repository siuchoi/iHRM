import unittest

from Test_iHRM.case.Test_user import TestEmpty

from Test_iHRM.case.Test_ihrm import TestIhrm

suite = unittest.TestSuite()

suite.addTest(TestIhrm("test_login_success"))
suite.addTest(TestEmpty("test_add"))
suite.addTest(TestEmpty("test_update"))
suite.addTest(TestEmpty("test_get"))
suite.addTest(TestEmpty("test_delete"))

runner = unittest.TextTestRunner()

runner.run(suite)
