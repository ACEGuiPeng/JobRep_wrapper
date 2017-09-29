class _CONST(object):
    def __setattr__(self, *_):
        raise SyntaxError('Trying to change a constant value')

    RESULT = 'result'
    SUCCESS = 'success'
    FAIL = 'fail'

    TASK_TYPE = 'type'
    MATCH_TASK_TYPE = 'match'
    RESULT_TASK_TYPE = 'result'
    USERTAGIDX_TASK_TYPE = 'usertagidx'

    METHOD_POST = 'POST'
    METHOD_GET = 'GET'

    SID = 'sid'
    CID = 'cid'
    ORDER_ID = 'order_id'

    LIST = 'list'
    UTF_8 = 'utf8'

    ETCD_HOST = 'ETCD_SERVICE_SERVICE_HOST'
    ETCD_PORT = 'ETCD_SERVICE_SERVICE_PORT'

    MONITOR_MODULE = 'monitor'
    STAT_MODULE = 'stat'
    SETTING_MODULE = 'setting'

    STAT_KEY = 'key'
    STAT_VALUE = 'value'

    SYSTEM_NAME = 'ygaui'
    SUBSYSTEM_NAME = 'oat'
    SUBSYSTEM_OAT = 'oat'
    SUBSYSTEM_OAM = 'oam'

    STAT_TOTAL_ORDER_NUM = 'stat_total_order_num'
    STAT_TOTAL_SEND_MSG_NUM = 'stat_total_send_msg_num'
    STAT_INVALID_USER_ORDER_NUM = 'stat_invalid_user_order_num'
    STAT_INVALID_SID_ORDER_NUM = 'stat_invalid_sid_order_num'
    STAT_INVALID_CID_ORDER_NUM = 'stat_invalid_cid_order_num'

    STAT_GET_AMZ_CID_INDEX_FAIL_NUM = 'stat_get_amz_cid_index_fail_num'
    STAT_UPDATE_TABLE_FAIL_NUM = 'stat_update_table_fail_num'
    STAT_TOTAL_RECV_MSG_NUM = 'stat_total_recv_msg_num'

    STAT_OAT_SET = [
        SYSTEM_NAME + '_' + SUBSYSTEM_OAT + '_' + STAT_TOTAL_ORDER_NUM,
        SYSTEM_NAME + '_' + SUBSYSTEM_OAT + '_' + STAT_TOTAL_SEND_MSG_NUM,
        SYSTEM_NAME + '_' + SUBSYSTEM_OAT + '_' + STAT_INVALID_USER_ORDER_NUM,
        SYSTEM_NAME + '_' + SUBSYSTEM_OAT + '_' + STAT_INVALID_SID_ORDER_NUM,
        SYSTEM_NAME + '_' + SUBSYSTEM_OAT + '_' + STAT_INVALID_CID_ORDER_NUM
    ]

    STAT_OAM_SET = [
        SYSTEM_NAME + '_' + SUBSYSTEM_OAM + '_' + STAT_TOTAL_RECV_MSG_NUM,
        SYSTEM_NAME + '_' + SUBSYSTEM_OAM + '_' + STAT_GET_AMZ_CID_INDEX_FAIL_NUM,
        SYSTEM_NAME + '_' + SUBSYSTEM_OAM + '_' + STAT_UPDATE_TABLE_FAIL_NUM
    ]

    MAX_BACK_FILE_NUM = 10
    MAX_BACK_FILE_SIZE = 256 * 1024 * 1024

    # happybase
    HAPPYBASE_POOL_SIZE = 2
    HAPPYBASE_RECONNECT_TIMES = 100
    HAPPYBASE_RECONNECT_WAIT_SECONDS = 5

    # mysql
    MYSQL_USERNAME = 'root'
    MYSQL_PWD = '123456'
    DB_URL = '192.168.0.16'
    DB_NAME = 'test_db'

    # tornado
    WEB_SERVER_PORT = 5000


CONST = _CONST()
