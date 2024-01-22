def nsecs_from_strings(date_strings):
    import iso8601
    from datetime import timezone
    times = []
    for string in date_strings:
      time_obj = iso8601.parse_date(string)
      times.append(time_obj.replace(tzinfo=timezone.utc).timestamp()*1e9)
    return times
