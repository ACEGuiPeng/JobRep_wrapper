# -*- coding:utf-8 -*-
import traceback

from flask import request
from flask_restful import Resource

from loggers.logger import log
from web.service.case.case_service import *
from web.service.landing_page.landing_page_record_service import *
from web.service.landing_page.landing_page_service import *
from web.service.material.material_record_service import *
from web.service.resource.resource_record_service import *


class Case(Resource):
    def get(self):
        result={}
        dict_data = request.args
        sorted_way = dict_data['sorted_way']
        page_no = dict_data['page_no']
        page_size = dict_data['page_size']
        case_result = select_case(dict_data, page_no, page_size, sorted_way)

        result['result'] = 'success'
        return result

    def post(self):
        json_data = request.get_json(force=True)
        try:
            case_data = json_data['case']
            lp_record_data = json_data['landing_page_record']
            mater_record_data = json_data['material_record']
            uid = case_data['uid']
        except KeyError as e:
            log.error(traceback.format_exc())
            return {'error_code': 56003, 'reason': 'the key is error or is not exits', 'result': 'failure'}
        except Exception as e:
            log.error(traceback.format_exc())
            return {'reason': str(e), 'result': 'failure'}
        case_id = insert_case(case_data)

        # 如果is_save为true，存落地页库，再存记录；否则只存记录
        if lp_record_data['is_save'] == 'true':
            for lp_record in lp_record_data:
                lp_ids = insert_landing_page(lp_record)
                lp_record['landing_page_id'] = lp_ids[0]
                lp_record['case_id'] = case_id
                lp_record_id = insert_landing_page_record(lp_record)

        for lp_record in lp_record_data:
            lp_record['case_id'] = case_id
        lp_record_ids = insert_landing_page_record(lp_record_data)

        for mater_record in mater_record_data:
            res_record = {}
            res_record['case_id'] = case_id
            res_record['resource_id'] = mater_record['id']
            res_record['uid'] = uid
            res_record_id = insert_resource_record(res_record)
            mater_record['resource'] = res_record_id
            mater_record['case_id'] = case_id
            mater_record_id = insert_material_record(mater_record)

        return {'result': 'success'}

    def put(self):
        try:
            json_data = request.get_json(force=True)
            case_data = json_data['case']
            lp_record_data = json_data['landing_page_record']
            mater_record_data = json_data['material_record']
            uid = case_data['uid']
        except KeyError as e:
            log.error(traceback.format_exc())
            return {'error_code': 56003, 'reason': 'the key is error or is not exits', 'result': 'failure'}
        except Exception as e:
            log.error(traceback.format_exc())
            return {'reason': str(e), 'result': 'failure'}
        message = update_case(json_data)
        return {'result': message}

    def delete(self):
        json_data = request.get_json(force=True)
        message = del_case(json_data)
        return {'result': message}
