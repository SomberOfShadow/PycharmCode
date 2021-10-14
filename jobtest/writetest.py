# -*- coding:UTF-8 -*-
# import datetime
import os
from datetime import datetime

# print(sys.getdefaultencoding())
import time


def get_latest_revision():
    return "CXXXX_2025_rf009"


# 文件不存在或者存在但是为空的时候，写入内容
path = 'C:\MySoftWare\Pycharm\PycharmTest\jobtest\\test\grat_status'
# print("%s does not exist" %(path))
if (not os.path.exists(path) or (os.path.exists(path) and not os.path.getsize(path))):
    with open(path, 'w') as fh:
        print(time.strftime("%Y-%m-%d", time.localtime()))
        # latest_revision = get_latest_revision()
        print(datetime.now().strftime('%Y-%m-%d'))
        fh.writelines(['No new FOSS scan ready for analysis.\n',
                       'Status: Idle\n',
                       get_latest_revision() + '\n',
                       'Latest_audit_id: 1390083\n',
                       'Date_of_latest_action: Not applicable\n',
                       'Date_of_process_started: ' + datetime.now().strftime('%Y-%m-%d') + '\n'])
    fh.close()

