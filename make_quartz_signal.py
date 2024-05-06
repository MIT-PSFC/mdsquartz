from datetime import datetime
from make_times import make_times

def make_quartz_signal(now:datetime, path:str, x:float, y:float):
    print(f'make_quartz_signal working on {path}')
    print(f'{y.dtype}')
    supported_types = ['float64', 'float32',]
    if y.dtype not in supported_types:
        msg = f'Only float64 values are currently supported. {path} is {y.dtype}'
        raise Exception(msg)
    channel_data= {
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
    print(f'make_quartz_signal returning {channel_data}')
    return channel_data
