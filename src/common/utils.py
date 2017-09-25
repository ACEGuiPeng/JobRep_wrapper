# -*- coding:utf-8 -*-
import logging
from functools import wraps
from json import loads as json_loads

from loggers.logger import log

from src.common.const import CONST

log_level_dict = {
    logging.DEBUG: log.debug,
    logging.INFO: log.info,
    logging.WARNING: log.warning,
    logging.ERROR: log.error,
    logging.CRITICAL: log.critical
}


def log_exception_decorate(level=logging.INFO):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                return result
            except Exception as error:
                log_level_dict[level]('{}'.format(error))

        return wrapper

    return decorate


debug_exception_decorate = log_exception_decorate(logging.DEBUG)
info_exception_decorate = log_exception_decorate(logging.INFO)
warning_exception_decorate = log_exception_decorate(logging.WARNING)
error_exception_decorate = log_exception_decorate(logging.ERROR)
critical_exception_decorate = log_exception_decorate(logging.CRITICAL)


def get_json_data_by_resp(resp):
    try:
        data_dict = json_loads(resp.content.decode(CONST.UTF_8))
    except Exception as err:
        log.error(str(err))
        return None
    return data_dict


def get_hb_value_to_string(value_dict, field_name):
    value = value_dict.get(field_name)
    if value is not None:
        return value.decode('utf-8')
    return None


def get_hb_value(value_dict, field_name):
    value = value_dict.get(field_name)
    if value is not None:
        return value
    return None


def get_hb_value_to_string_trim(value_dict, field_name):
    value = value_dict.get(field_name)
    if value is not None:
        return " ".join(value.decode('utf-8').split())
    return None
