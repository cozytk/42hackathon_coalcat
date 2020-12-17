from flask import Flask
from flask import request
from measure_distance import measure_distance
from find_coalition_with_id import find_coalition_with_id
from find_coalition_with_id import get_access_token
from control_led import turn_on_red_led, turn_off_red_led, turn_on_green_led, turn_off_green_led

from apscheduler.schedulers.background import BackgroundScheduler
sched = BackgroundScheduler()

gun_hungry = 10
gon_hungry = 20
gam_hungry = 30
lee_hungry = 40

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world'

@app.route('/get_coalition/')
def get_coalition():
    intra_name = request.args.get('name', 'iwoo')
    return str(find_coalition_with_id(intra_name))

@app.route('/get_distance')
def get_distance():
    return str(measure_distance())

@app.route('/is_ready')
def is_ready():
    start_point_distance = 10.0
    food_distance = float(measure_distance())
    print(str(food_distance))
    if (start_point_distance - 5 <= food_distance <= start_point_distance + 5):
        print("correct! turn on green led!")
        turn_on_green_led()
        turn_off_green_led()
        return "true"
    turn_on_red_led()
    turn_off_red_led()
    return "false"

@app.route('/get_hungry')
def get_hungry():
    coal_name = request.args.get('coal_name')
    value = request.args.get('value')
    print("coal_name: " + coal_name + " value: " + value)

    if coal_name == "gun":
        global gun_hungry
        gun_hungry += int(value)
        if gun_hungry < 0:
            gun_hungry = 0
        elif gun_hungry > 100:
            gun_hungry = 100

        print("gun_hungry: " + str(gun_hungry))

        return str(gun_hungry)
    elif coal_name == "gon":
        global gon_hungry
        print(gon_hungry)
        gon_hungry += int(value)
        if gon_hungry < 0:
            gon_hungry = 0
        elif gon_hungry > 100:
            gon_hungry = 100

        print("gon_hungry: " + str(gon_hungry))

        return str(gon_hungry)
    elif coal_name == "gam":
        global gam_hungry
        print(gam_hungry)
        gam_hungry += int(value)
        if gam_hungry < 0:
            gam_hungry = 0
        elif gam_hungry > 100:
            gam_hungry = 100

        print("gam_hungry: " + str(gam_hungry))

        return str(gam_hungry)
    elif coal_name == "lee":
        global lee_hungry
        print(lee_hungry)
        lee_hungry += int(value)
        if lee_hungry < 0:
            lee_hungry = 0
        elif lee_hungry > 100:
            lee_hungry = 100

        print("lee_hungry: " + str(lee_hungry))

        return str(lee_hungry)
    return str(gun_hungry)

@app.route('/feeding_success')
def reduce_gun_hungry():
    print("======================feeding success========================")
    coal_name = request.args.get('coal_name')
    value = request.args.get('value')
    print("coal_name: " + coal_name + " value: " + value)
    print("=============================================================")
    if coal_name == "gun":
        global gun_hungry
        print(gun_hungry)
        gun_hungry += int(value)
        if gun_hungry < 0:
            gun_hungry = 0
        elif gun_hungry > 100:
            gun_hungry = 100
        return str(gun_hungry)
    elif coal_name == "gon":
        global gon_hungry
        print(gon_hungry)
        gon_hungry += int(value)
        if gon_hungry < 0:
            gon_hungry = 0
        elif gon_hungry > 100:
            gon_hungry = 100
        return str(gon_hungry)
    elif coal_name == "gam":
        global gam_hungry
        print(gam_hungry)
        gam_hungry += int(value)
        if gam_hungry < 0:
            gam_hungry = 0
        elif gam_hungry > 100:
            gam_hungry = 100
        return str(gam_hungry)
    elif coal_name == "lee":
        global lee_hungry
        print(lee_hungry)
        lee_hungry += int(value)
        if lee_hungry < 0:
            lee_hungry = 0
        elif lee_hungry > 100:
            lee_hungry = 100
        return str(lee_hungry)
    return "Cats be happy.."

if __name__ == '__main__':
    get_access_token()
    job = sched.add_job(get_access_token, 'interval', seconds=30)
    sched.start()
    app.run(debug=True, port=80, host='0.0.0.0')
