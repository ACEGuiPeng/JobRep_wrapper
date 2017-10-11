# -*- coding:utf-8 -*-
import uuid

import requests

random_num = uuid.uuid4()


def send_json_data():
    resp = requests.post('http://127.0.0.1:5000/ygfbad/web/cases', json={
        "sid": "{}".format(random_num),
        "timestamp": "{}".format(random_num),
        "case_name": "test_case",
        "target_id": "123460",
        "material_timestamp": "123460",
        "status": "123460",
        "bidding": "123460"
    })
    resp = requests.get('http://127.0.0.1:5000/ygfbad/web/cases', json={
        "sid": "{}".format(random_num),
        "timestamp": "{}".format(random_num),
        "case_name": "test_case",
        "target_id": "123460",
        "material_timestamp": "123460",
        "status": "123460",
        "bidding": "123460"
    })
    resp = requests.put('http://127.0.0.1:5000/ygfbad/web/cases', json={
        "sid": "{}".format(random_num),
        "timestamp": "{}".format(random_num),
        "case_name": "test_case",
        "target_id": "123460",
        "material_timestamp": "123460",
        "status": "123460",
        "bidding": "123460"
    })
    resp = requests.delete('http://127.0.0.1:5000/ygfbad/web/cases', json={
        "sid": "{}".format(random_num),
        "timestamp": "{}".format(random_num),
        "case_name": "test_case",
        "target_id": "123460",
        "material_timestamp": "123460",
        "status": "123460",
        "bidding": "123460"
    })

    # material
    resp = requests.post('http://127.0.0.1:5000/ygfbad/web/maters', json={
        "sid": "{}".format(random_num),
        "timestamp": "{}".format(random_num),
        "content": "test_content"
    })
    resp = requests.get('http://127.0.0.1:5000/ygfbad/web/maters', json={
        "sid": "{}".format(random_num),
        "timestamp": "{}".format(random_num),
        "content": "test_content"
    })
    resp = requests.put('http://127.0.0.1:5000/ygfbad/web/maters', json={
        "sid": "{}".format(random_num),
        "timestamp": "{}".format(random_num),
        "content": "test_content"
    })
    resp = requests.delete('http://127.0.0.1:5000/ygfbad/web/maters', json={
        "sid": "{}".format(random_num),
        "timestamp": "{}".format(random_num),
        "content": "test_content"
    })
