from datetime import datetime
def get_day():
    today_date = datetime.now()
    day = today_date.strftime("%A")
    time = today_date.strftime("%H")
    current_time = {
        "day": day,
        "time": time
    }
    return current_time


def time_check(current_time, class_time):
    time = int(current_time)
    class_starting_time = int(class_time[:2])-1
    class_ending_time = int(class_time[6:8])
    if class_starting_time <= time <= class_ending_time:
        return True
    else:
        return False



