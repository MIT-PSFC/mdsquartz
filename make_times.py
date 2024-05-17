from datetime import datetime
def make_times(now:datetime, times:float):
  import time
  from datetime import date, datetime, timezone, timedelta
  ans = []
  for t in times:
    ans.append((now + timedelta(seconds=float(t))).isoformat())
  return ans
