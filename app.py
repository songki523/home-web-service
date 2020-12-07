from flask import Flask, request, abort
from flask import render_template, send_from_directory
from csv_handler import CsvHandler
import datetime, os

app = Flask(__name__)
app.config["CLIENT_CSV"] = os.getcwd() + "/csv"

_today = datetime.date.today()
_year = _today.year

@app.route('/', methods=['GET', 'POST'])
def index():
    print(os.getcwd())
    if request.method == 'POST':
        _collections = []
        name = request.form['name']
        month = request.form['month']
        days = request.form['days']
        
        date_list = days.split(",")

        year = is_month_january(month, _year)

        csvhandler = CsvHandler("DayShift-" + str(_today))

        for day in date_list:
            _collections.append(
                {"Subject": "{} Day Shift".format(name),
                "Start Date": "{}/{}/{}".format(month, day, year)}
            )
        
        csvhandler.store_into_csv(_collections)

        try:
            return send_from_directory(app.config["CLIENT_CSV"], filename=csvhandler.filename + ".csv", as_attachment=True)
        except FileNotFoundError:
            abort(404)

    return render_template('index.html')

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

# Generate Calendar to Next Year when a user enters next year
def is_month_january(_month, _year):
    ret = 0
    if int(_month) == 1:
        ret = int(_year) + 1
    else:
        ret = _year

    return ret

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug='True')
