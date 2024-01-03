def usecs_from_strings(dt_strings):
 
    def standardize_datetime_frac(dt_str):
        parts = dt_str.split('.')
        if len(parts) == 1:
            return (parts[0])
        frac = parts[1][:6]
        frac += '0' * (6 - len(frac))
        return parts[0] + "." + frac
    import numpy as np
    from datetime import datetime

    def convert_to_nsec(dt_str):
        dt = datetime.fromisoformat(standardize_datetime_frac(dt_str.replace('Z', '')))
        timestamp = dt.timestamp() 
        return int(timestamp * 1e9)

    return np.array(list(map(convert_to_nsec, dt_strings)))

