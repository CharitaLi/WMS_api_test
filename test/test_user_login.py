import json
import sys
sys.path.append("E:/WMSAPITest/test")
from lib.read_excel import *
from lib.case_log import log_case_info
import unittest
import requests


class TestUserLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.data_list = excel_to_list("E:/WMSAPITest/test/data/test_user_data.xlsx", "TestUserLogin")

    def test_user_login_normal(self):
        
        case_data = get_test_data(self.data_list,'test_user_login_normal')
        if not case_data:
            print('用例不存在')
        loginurl = case_data.get('url')
        loginuser = json.loads(case_data.get('data'))
        expect_res_success = case_data.get('expect_res_success')
        res= requests.post(url=loginurl,data=loginuser,auth=("admin","apple.1234"))
        log_case_info('test_user_login_normal',loginurl,loginuser,expect_res_success,res.json()['success'])

        self.assertEqual(expect_res_success,res.json()['success'])
    

    def test_user_login_UserNameError(self):
        case_data = self.data_list[1]
        test_url = case_data.get("url")
        test_user = case_data.get("data")
        test_user = json.loads(test_user)
        test_success = case_data.get("expect_res_success")
        test_message = case_data.get("expect_res_message")

        res = requests.post(url=test_url,data=test_user,auth=("admin","apple.1234"))
        log_case_info('test_user_login_UserNameError',test_url,test_user,test_success,res.json()['success'])
        log_case_info('test_user_login_UserNameError',test_url,test_user,test_message,res.json()['message'])

        self.assertEqual(test_success,res.json()['success'])
        self.assertEqual(test_message,res.json()['message'])


    def test_user_login_UserPasswordError(self):
        case_data = self.data_list[2]
        test_url = case_data.get("url")
        test_user = case_data.get("data")
        test_user = json.loads(test_user)
        test_success = case_data.get("expect_res_success")
        test_message = case_data.get("expect_res_message")

        res = requests.post(url=test_url,data=test_user,auth=("admin","apple.1234"))
        log_case_info('test_user_login_UserNameError',test_url,test_user,test_success,res.json()['success'])
        log_case_info('test_user_login_UserNameError',test_url,test_user,test_message,res.json()['message'])
        self.assertEqual(test_success,res.json()['success'])
        self.assertEqual(test_message,res.json()['message'])


# if __name__ == '__main__':  
#     unittest.main()   
   