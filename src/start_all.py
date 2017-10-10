# -*- coding:utf-8 -*-
from initializer.initializer import init, de_init
from loggers.logger import log
from web.app import run_web_service, stop_web_service


def start_all():
    init()
    run_web_service()


if __name__ == '__main__':
    log.info('enter main...')

    try:
        start_all()
    except Exception as error:
        log.fatal(str(error))
        de_init()
        stop_web_service()
        exit(0)
