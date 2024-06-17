#! python
import numpy as np
import random
import quartz
import tempfile
from datetime import datetime, timezone
from make_quartz_signal import make_quartz_signal

NUM_TRYS = 100
ONED_SIZE = 100000
ONED_SMALLEST = 10000
TWOD_SIZE = (1000,1000)
TWOD_SMALLEST = (10, 10)
MAX_TIME = 2.5

sampl = np.random.uniform(low=-10, high=10, size=(ONED_SIZE))
oned_times = np.arange(0., MAX_TIME, MAX_TIME/ONED_SIZE)

twod_size = TWOD_SIZE[0]*TWOD_SIZE[1]
twod = np.random.uniform(low=-10, high=10, size=(twod_size)).reshape(TWOD_SIZE)
twod_times = np.arange(0., MAX_TIME, MAX_TIME/TWOD_SIZE[0])

dataset = f"trial-dataset"
data_registry_client = quartz.DataRegistryClient(quartz.PRODUCTION_DATA_REGISTRY_URL)
data_access_client = quartz.DataAccessClient(quartz.PRODUCTION_DATA_ACCESS_URL)
now = datetime.now(timezone.utc)

run = data_registry_client.create_run(10, name=f"trial_{random.randint}", description=f"test data set", tags=[str(now), ])

run_id = run["id"]
print(f'The runid is {run_id}')

#
# upload a file so that the dataset is not empty when we try to write to it
#
with tempfile.NamedTemporaryFile() as f:
    data_access_client.upload_file(run_id, f.name, dataset=dataset)

for idx in range(NUM_TRYS):
    try:
        if random.randrange(0,100) % 2:
          path=f'SIGNAL_{idx}'
          nsamp = random.randrange(ONED_SMALLEST, ONED_SIZE-1, 1)
          channel_data = make_quartz_signal(now, path, oned_times[0:nsamp], sampl[0:nsamp])
          guid = data_access_client.write_channel_data(run_id, dataset, channel_data)
        else:
          path=f'TWOD_{idx}'
          nsamp = random.randrange(TWOD_SMALLEST[1], TWOD_SIZE[1]-1, 1)
          channel_data = make_quartz_signal(now, path, twod_times[0:nsamp], twod[0:nsamp,0:random.randrange(1,100)])
          guid = data_access_client.write_channel_data(run_id, dataset, channel_data)          
    except Exception as e:
        print(path, e)

