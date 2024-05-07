
def getquartz(run_id, signal_name, start_time, end_time, zero_time, dataset):
    """
    return an MDSplus signal from stored QUARTZ data

    Usage:
      getquartz(guid, channel_name, start_time, end_time, zero_time)

    Parameters:
      guid - string GUID of the quartz dataset
      channel_name - string name of the 'channel' to return
      start_time - string (ISO 8601 format) return data labeled starting at this time
      end_time - string (ISO 8601 format) return data labeled ending at this time
      zero_time - string (ISO 8601 format) specify the time which 0.0 corresponds to.
    Usage in TDI:
        getquartz(guid, channel_name, start_time, end_time, zero_time)

        returns an MDSplus.Signal

        for example:
            _sig = getquartz("885c9dd7-24b1-4789-b4b2-f309f093be28","finj.in_chan_1","2023-09-21T22:39:00","2023-09-21T22:40:00","2023-09-21T22:39:00")

    NOTE: python type hints are not used since the arguments can be either Python strings 
          or MDSplus strings .       
    """
    import MDSplus
    import quartz
    import datetime as dt
    from datetime import timezone as tz
    from zoneinfo import ZoneInfo
    import numpy as np
    from nsec_from_string import nsec_from_string
    from nsecs_from_strings import nsecs_from_strings
    from dateutil.parser import parse
    data_access_client = quartz.DataAccessClient(quartz.PRODUCTION_DATA_ACCESS_URL)
    chnls = [str(signal_name)]
    if start_time.__class__ == MDSplus.tree.TreeNode:
        start_time = str(start_time.data())
    start = parse(str(start_time))
    if end_time.__class__ == MDSplus.tree.TreeNode:
        end_time = str(end_time.data())
    end = parse(str(end_time))
    if run_id.__class__ == MDSplus.tree.TreeNode:
        run_id = run_id.data()
    ans =  data_access_client.read_channel_data(str(run_id),
                                             channels = chnls,
                                             start = start,
                                             end = end,
                                             dataset = dataset)
    times = np.array(nsecs_from_strings(ans[0]['children'][0]['data']['times']))
    if zero_time.__class__ == MDSplus.tree.TreeNode:
        zero_time = zero_time.data()
    times -= nsec_from_string(zero_time)
    times *= 1E-9
    values = ans[0]['children'][0]['data']['values']
    return MDSplus.Signal(np.array(values), None, times)
