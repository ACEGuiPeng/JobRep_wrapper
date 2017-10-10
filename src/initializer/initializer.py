# -*- coding:utf-8 -*-

from initializer.base import BS_INITIALIZER
from loggers.logger import log


def init():
    try:
        BS_INITIALIZER.initialize()
    except Exception as err:
        log.fatal(str(err))
        raise err


def de_init():
    BS_INITIALIZER.de_initialize()
