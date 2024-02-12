import re

def preprocess_name(name):
    if(bool(re.search('^[a-zA-Z0-9]*$',name))==True):
        return True
    else:
        return False
    
def preprocess_time(time_str):
    hours, minutes, seconds = time_str.split(':')
    hours = int(hours) % 24
    return f'{hours:02d}:{minutes}:{seconds}'