#! python
import os
import pprint
import sys
pprint.pprint(dict(os.environ))
sys.path.append("usr-local-mdsplus-debug/python")
os.environ['LD_LIBRARY_PATH'] = ":usr-local-mdsplus-debug/lib"

import quartz
import MDSplus
from datetime import datetime, timezone
from make_quartz_signal import make_quartz_signal
run_id = "8eed82c5-bec8-430f-8451-665631214fc6"
dataset = "1160930034-analysis"
data_access_client = quartz.DataAccessClient(quartz.PRODUCTION_DATA_ACCESS_URL)
now = datetime.now(timezone.utc)
tree = MDSplus.Tree('analysis',1160930034)
signals = tree.getNodeWild('***', 'signal')

for signal in signals:
    try:
        path = signal.fullpath
        y = signal.data()
        x = signal.dim_of().data()
        channel_data = make_quartz_signal(now, path, x, y)
        guid = data_access_client.write_channel_data(run_id, dataset, channel_data)
        print(path, guid)
    except Exception as e:
        print(path, e)

