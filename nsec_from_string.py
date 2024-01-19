def nsec_from_string(date_string):
    import iso8601
    from datetime import timezone
    time_obj = iso8601.parse_date(time_str)
    return time_obj.replace(tzinfo=timezone.utc).timestamp()*1e9
