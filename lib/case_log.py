import sys
sys.path.append("..")
from config.config import *
import json

def log_case_info(case_name, url, data, ex_result, ac_result): 
    if isinstance(data,dict):
        data = json.dumps(data, ensure_ascii=False)  # 如果data是字典格式，转化为字符串
    
    logging.info("测试案例: {}".format(case_name))
    logging.info("url: {}".format(url))
    logging.info("测试数据: {}".format(data))
    logging.info("期望结果: {}".format(ex_result))
    logging.info("实际结果: {}".format(ac_result))

