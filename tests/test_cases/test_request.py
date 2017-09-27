# -*- coding:utf-8 -*-
import requests

if __name__ == '__main__':
    resp = requests.post('http://127.0.0.1:5000/ygfbad/web/cases', json={
        "sid": "123461",
        "timestamp": "123461",
        "case_name": "test_case",
        "target_id": "123460",
        "material_timestamp": "123460",
        "status": "123460",
        "bidding": "123460"
    })
