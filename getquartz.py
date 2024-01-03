
def getquartz(run_id, signal_name, start_time):
    import MDSplus
    import quartz
    import datetime as dt
    from datetime import timezone as tz
    from zoneinfo import ZoneInfo
    import numpy as np
    from usecs_from_strings import usecs_from_strings
    data_access_client = quartz.DataAccessClient(quartz.PRODUCTION_DATA_ACCESS_URL)
    chnls = [str(signal_name)]
    end = dt.datetime(2023,9,21,18,40,tzinfo = ZoneInfo("US/Eastern"))
    strt = end - dt.timedelta(minutes = 1) 
    ans =  data_access_client.read_channel_data(str(run_id),
                                             channels = chnls,
                                             start = strt.astimezone(ZoneInfo("UTC")),
                                             end = end.astimezone(ZoneInfo("UTC")))
    times = usecs_from_strings(ans[0]['children'][0]['data']['times'])
    times -= usecs_from_strings([start_time])[0]
    times = MDSplus.Float64(times)*1E-6
    values = ans[0]['children'][0]['data']['values']
    return MDSplus.Signal(np.array(values), None, times)
