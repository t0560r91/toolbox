import numpy as np
import pandas as pd
from datetime import datetime, timedelta    


def datespace(start, end, step=1):
    """
    INPUT:
        start: date string in '%Y-%m-%d'
        end: date string in '%Y-%m-%d'

    OUTPUT:
        list of datetime.date objects ranging from the given start and end date

    """
    if start <= end:
        a = datetime.strptime(start, '%Y-%m-%d')
        z = datetime.strptime(end, '%Y-%m-%d')
        result = []
        result.append(a.date())
        while z > a:
            a += timedelta(days=step)
            if a <= z:
                result.append(a.date())
        return result
    else: 
        raise ValueError('Start Date cannot be before End Date.')


def timespace(start, end, step=60):
    """
    input
    ==========================
    start: time string in '%H:%M:%S'
    end: time string in '%H:%M:%S'

    output
    ==========================
    list of datetime.time objects ranging from the given start and end time

    """
    if start <= end:
        a = datetime.strptime(start, '%H:%M:%S')
        z = datetime.strptime(end, '%H:%M:%S')
        result = []
        result.append(a.time())
        while z > a:
            a += timedelta(seconds=step)
            if a <= z:
                result.append(a.time())
        return result
    else: 
        raise ValueError('Start Date cannot be before End Date.')


def datetimespace(start, end, stepunit='days', stepsize=1):
    """
    input
    ==========================
    start: time string in '%Y-%m-%d %H:%M:%S'
    end: time string in '%Y-%m-%d %H:%M:%S'

    output
    ==========================
    list of datetime objects ranging from the given start and end datetime

    """
    if start <= end:
        a = datetime.strptime(start, '%Y-%m-%d %H:%M:%S')
        z = datetime.strptime(end, '%Y-%m-%d %H:%M:%S')
        result = []
        result.append(a)
        while z > a:
            a += timedelta(stepunit=stepsize)
            if a <= z:
                result.append(a)
        return result
    else: 
        raise ValueError('Start Date cannot be before End Date.')


def scale_time(time):
    """
    "Scale and split time to sin_cos_time"
    
    INPUT:
        start: time string in '%H:%M'
    
    OUTPUT:
        sin_time, cos_time
    """
    td = timedelta(hours=time.hour, minutes=time.minute)
    in_minutes = td.seconds//60
    scaler = 2*np.pi/1440
    halfway_scaled = in_minutes * scaler
    return np.sin(halfway_scaled), np.cos(halfway_scaled)




# DATE & TIME
#####################################################
def parse_datetime(time_str, out_format='datetime'):
    """
    "reads time_str in any format and writes a datetime, date, or time obejct"
    
    INPUT:
        time_str: time string in any format
        out_format: datetime, date, or time
    
    OUTPUT:
        parsed time_string
    """
    in_formats = ['%Y-%m-%dT%H:%M:%S.%f', '%Y-%m-%d %H:%M:%S.%f', 
                  '%Y-%m-%dT%H:%M:%S', '%Y-%m-%d %H:%M:%S', 
                  '%Y-%m-%dT%I:%M%p', '%Y-%m-%d %I:%M%p',
                  '%Y-%m-%d']
    for f in in_formats:
        try:
            if out_format == 'datetime':
                return datetime.strptime(time_str, f)
            elif out_format == 'date':
                return datetime.strptime(time_str, f).date()
            elif out_format == 'time':
                return datetime.strptime(time_str, f).time()
        except:
            continue


def reformat_time_string(time_str):
    """
    "reads time_str in any format and reformats it to 24 hour cycle or 12 hour cycle 
    which ever was not the original format."

    INPUT:
        time_str: time string in any format
    
    OUTPUT:
        time_str: time string reformated
    """
    dt = parse_datetime(time_str)
    reformat = datetime.strftime(dt, '%Y-%m-%d %I:%M%p')
    if reformat != time_str:
        return reformat
    else:
        return datetime.strftime(dt, '%Y-%m-%d %H:%M:S')




