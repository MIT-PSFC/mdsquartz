import quartz

import time
from datetime import date, datetime, timezone, timedelta

run_id = "8eed82c5-bec8-430f-8451-665631214fc6"
dataset = "test-dataset"
data_access_client = quartz.DataAccessClient(quartz.PRODUCTION_DATA_ACCESS_URL)

# Creating a distribution of test times.
times = []
for i in range(5):
    t = datetime.now(timezone.utc)
    time.sleep(1)
    times.append(t)

# Building channel data consisting of two channels within a channel group.
channel_data = {
    "channels": [
        {
            "name": "group",
            "type": "channel_group",
            "children": [
                {"name": "current", "type": "float64", "data": {
                    "times": times,
                    "values": [3.14, 2.718, -32.5, 1.0, -111111]
                }},
                {"name": "voltage", "type": "float64", "data": {
                    "times": times,
                    "values": [0.9, -0.888, 0.3, 1.0, 2.3]
                }},
            ],
        },
    ],
}

# Writing channel data to the test run and dataset.
data_access_client.write_channel_data(run_id, dataset, channel_data)

# Grabbing data from the last day.
now = datetime.now(timezone.utc)
start = (now - timedelta(days=1))

# Querying the channels.
query_channels = ["group.current", "group.voltage"]
data = data_access_client.read_channel_data(run_id, dataset=dataset, channels=query_channels, start=start, end=now)
print(data)

