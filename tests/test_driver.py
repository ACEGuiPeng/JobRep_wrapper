# -*- coding:utf-8 -*-


import sys

import time
from threading import Thread

from coverage import coverage

from test_api.send_json_data import send_json_data
from web.app import run_web_service, stop_web_service

# 设置覆盖测试的初始状态
if __name__ == '__main__':
    undebug = True

    if len(sys.argv) > 1:
        if sys.argv[1] == 'true':
            undebug = True
        elif sys.argv[1] == 'false':
            undebug = False

    # coverage开始
    cov = None
    if undebug:
        cov = coverage(branch=True, source=["../src/wrappers", "../src/web"])
        cov.start()

    Thread(target=run_web_service).start()
    time.sleep(3)
    send_json_data()
    time.sleep(3)
    Thread(target=stop_web_service).start()

    # coverage结束
    if undebug:
        cov.stop()
        cov.html_report(directory="test_result/htmlvov")
        cov.xml_report(outfile="test_result/coverage.xml")
