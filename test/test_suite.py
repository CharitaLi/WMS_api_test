import unittest
from test_user_login import TestUserLogin
import sys
sys.path.append("E:/WMSAPITest/test")
from lib.HTMLTestReportCN import HTMLTestRunner 

# 添加单个用例
# suite = unittest.TestSuite()
# suite.addTest(TestUserLogin('test_user_login_normal')) 

# 运行该类所有用例
suite = unittest.makeSuite(TestUserLogin) 

# 运行测试集
# unittest.TextTestRunner(verbosity=2).run(suite) 

# txt形式测试报告
# with open("result.txt","w") as f:
#     unittest.TextTestRunner(stream=f,verbosity=2).run(suite) 

# 网页形式测试报告
f = open("E:/WMSAPITest/test/report/report.html", 'wb') 
HTMLTestRunner(stream=f,title="Api Test",description="测试描述").run(suite)
f.close()

