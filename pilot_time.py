from datetime import datetime

def getCurrentTime():
    now = datetime.now()
    mins = now.strftime("%M")
    if int(now.strftime("%H")) > 12:
        hour = int(now.strftime("%H")) - 12
        timeOfDay = "PM"
    elif int(now.strftime("%H")) == 12:
        hour = int(now.strftime("%H"))
        timeOfDay = "PM"
    else:
        hour = int(now.strftime("%H"))
        timeOfDay = "AM"
    return str(hour)+':'+str(mins)+' '+timeOfDay
