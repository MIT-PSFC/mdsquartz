#! python
import os
import pprint
import sys
import tempfile
pprint.pprint(dict(os.environ))
sys.path.append("usr-local-mdsplus-debug/python")
os.environ['LD_LIBRARY_PATH'] = ":usr-local-mdsplus-debug/lib"

import quartz
import MDSplus
from datetime import datetime, timezone
from make_quartz_signal import make_quartz_signal
shotnumber = 1160930034
treename = 'analysis'
dataset = f"{shotnumber}-{treename}"
data_registry_client = quartz.DataRegistryClient(quartz.PRODUCTION_DATA_REGISTRY_URL)
data_access_client = quartz.DataAccessClient(quartz.PRODUCTION_DATA_ACCESS_URL)
now = datetime.now(timezone.utc)

tree = MDSplus.Tree(treename,shotnumber)
signals = tree.getNodeWild('***', 'signal')

run = data_registry_client.create_run(10, name=f"analysis_{shotnumber}", description=f"{treename} tree for shot {shotnumber}", tags=[str(now), ])


run_id = run["id"]
with tempfile.NamedTemporaryFile() as f:
    data_access_client.upload_file(run_id, f.name, dataset=dataset)
for signal in signals:
    try:
        path = signal.fullpath
        y = signal.data()
        x = signal.dim_of().data()
        channel_data = make_quartz_signal(now, path, x, y)
        print(f"data_access_client.write_channel_data({run_id}, {dataset}, channel_data)")
        guid = data_access_client.write_channel_data(run_id, dataset, channel_data)
        print(path, guid)
    except Exception as e:
        print(path, e)

