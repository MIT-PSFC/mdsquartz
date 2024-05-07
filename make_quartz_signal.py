from datetime import datetime
from make_times import make_times
import json
def make_quartz_signal(now:datetime, path:str, x:float, y:float):
    print(f'make_quartz_signal working on {path}')
    print(f'{y.dtype}')
    supported_types = ['float64', 'float32',]
    if y.dtype not in supported_types:
        msg = f'Only float64 values are currently supported. {path} is {y.dtype}'
        raise Exception(msg)    
    channel_data = {
        "channels": [
            {
                "name": path.replace('::','.').replace(':','.').replace('\\',''),
                "type": "channel_group",
                "children": [
                    {"name": "value", "type": "float64", "data": {
                        "times": make_times(now,x),
                        "values": y.tolist(),
                    }},
                ],
            },
        ],
    }
#    print(f'make_quartz_signal returning {channel_data}')
    print(f'make_quartz_signal returning {json.dumps(channel_data, indent=4)}')
    return channel_data

"""     channel_data = {
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
} """


"""     channel_data= {
        "channels": [
            {
                "name": path.replace('::','.').replace(':','.').replace('\\',''),
                "type": "channel_group",
                "children": [
                    {"name": "value", "type": "float64", "data": {
                        "times": make_times(now,x),
                        "values": y.tolist(),
                    }},
                ],
            },
        ],
    }
 """    
