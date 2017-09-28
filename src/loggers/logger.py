# -*- coding:utf-8 -*-

import logging
import os
from distutils.dir_util import mkpath
from logging import handlers

from src.common.const import CONST

logging.basicConfig()
logger = logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)


def get_logger_name():
    return CONST.SYSTEM_NAME + '_' + CONST.SUBSYSTEM_NAME


def get_logger_file_name(logger_name):
    return logger_name + '.log'


def get_or_create_log_path(logger_name):
    storage_path = '../data/log/'
    if not os.path.exists(storage_path):
        mkpath(storage_path)

    return storage_path


def get_logger_format():
    fmt = '[%(asctime)s]'
    fmt += '-[%(levelname)s]'
    fmt += '-[%(process)d]'
    fmt += '-[%(threadName)s]'
    fmt += '-[%(thread)d]'
    fmt += '-[%(filename)s:%(lineno)s]'
    fmt += ' # %(message)s'
    return fmt


def add_rotating_file_handler(logger, logger_name, formatter):
    file_name = get_or_create_log_path(logger_name) + get_logger_file_name(logger_name)
    handler = handlers.RotatingFileHandler(
        file_name, maxBytes=CONST.MAX_BACK_FILE_SIZE, backupCount=CONST.MAX_BACK_FILE_NUM)
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def add_stream_handler(logger, formatter):
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)


def init_logger(log_level):
    logger_name = get_logger_name()
    logger = logging.getLogger(logger_name)

    formatter = logging.Formatter(get_logger_format())
    add_rotating_file_handler(logger, logger_name, formatter)
    add_stream_handler(logger, formatter)

    logger.setLevel(log_level)
    return logger


log = init_logger(logging.INFO)
