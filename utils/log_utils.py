# -*-coding:utf-8-*-

import logging


def init_logger():
    logs = logging.getLogger()
    logs.setLevel(logging.INFO)
    f = logging.Formatter('%(asctime)s %(levelname)s [%(pathname)s/%(funcName)s] ==> %(message)s')
    s = logging.StreamHandler()
    s.setFormatter(f)
    logs.addHandler(s)
    return logs


logger = init_logger()
