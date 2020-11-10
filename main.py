import pilot_bt_ctl, pilot_time, pilot_sys_info, pilot_car_info
from flask import Flask, request, render_template
import threading

app = Flask(__name__)
app.debug = True

# The "home" page for the car interface. Displays music information via musicInfo function 
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template("home.html")

# Temp page to display OBDII/CAN bus sensor data. 
@app.route("/carDetails", methods=['GET', 'POST'])
def carDetails():
    return render_template("carInfo.html")

# Method of retrieval for the most current time from the RTC module on the Pi
@app.route("/ctime", methods=['GET', 'POST'])
def currentTime():
    if request.method == "POST":
        return pilot_time.getCurrentTime()

# Method of retrieval for the OBDII/CAN bus sensor data
@app.route("/carInfo", methods=['GET', 'POST'])
def carInfo():
    if request.method == "POST":
        pilot_car_info.get_CarInfo()
        return pilot_car_info.gas_level+'# # '+pilot_car_info.speed+'# # '+pilot_car_info.RPM+'# # '+pilot_car_info.eng_load

# Method of retrieval for the bluetooth metadata
@app.route("/musInfo", methods=['GET', 'POST'])
def musInfo():
    if request.method == "POST":
        return pilot_bt_ctl.title+'# # '+pilot_bt_ctl.artist+'# # '+pilot_bt_ctl.album

# Method of retrieval for Pi system data, currently just CPU load
@app.route("/sysInfo", methods=['GET', 'POST'])
def sysInfo():
    if request.method == "POST":
        return pilot_sys_info.CPUGetState()

# Endpoint hit to pause/play a track
@app.route("/ppTrack", methods=['GET', 'POST'])
def ppTrack():
    if request.method == "POST":
        if pilot_bt_ctl.mediaGetState() == 'paused':
            pilot_bt_ctl.mediaControl('play')
        elif pilot_bt_ctl.mediaGetState() =='play':
            pilot_bt_ctl.mediaControl('paused')

# Endpoint hit to skip to the next track
@app.route("/nextTrack", methods=['GET', 'POST'])
def nextTrack():
    if request.method == "POST":
        pilot_bt_ctl.mediaControl('next')

# Endpoint hit to go to the start of a track/the previous track
@app.route("/lastTrack", methods=['GET', 'POST'])
def lastTrack():
    if request.method == "POST":
        pilot_bt_ctl.mediaControl('last')

if __name__ == "__main__":
    # Starts the DBUS loop via threading to retrieve bluetooth metadata
    metaThr = threading.Thread(target=pilot_bt_ctl.initMetadata, name = 'metadata')
    metaThr.start()

    # Starts the flask app
    app.run()
