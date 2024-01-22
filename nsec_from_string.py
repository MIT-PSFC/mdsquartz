def nsec_from_string(date_string):
    import iso8601
    from datetime import timezone
    print(date_string)
    time_obj = iso8601.parse_date(str(date_string))
    return time_obj.replace(tzinfo=timezone.utc).timestamp()*1e9
