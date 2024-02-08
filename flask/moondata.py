from flask import Flask, render_template, request, jsonify, json, redirect, url_for
from pymongo import MongoClient
app = Flask(__name__)

# designate upper and lower limit
@app.route('/time')
def formPage():
    return render_template('Time.html')

@app.route('/submit', methods=['POST'])
def submit():
    # upper time limit
    Myear = request.form['Myear']
    Mmon = request.form['Mmon']
    Mdate = request.form['Mdate']
    Mhr = request.form['Mhr']
    Mmin = request.form['Mmin']
    Msec = request.form['Msec']
    maxi = Myear + Mmon + Mdate + Mhr + Mmin + Msec
    # lower time limit
    myear = request.form['myear']
    mmon = request.form['mmon']
    mdate = request.form['mdate']
    mhr = request.form['mhr']
    mmin = request.form['mmin']
    msec = request.form['msec']
    mini = myear + mmon + mdate + mhr + mmin + msec
    print("Upper limit ", mini, " => ", maxi)
    return redirect(url_for('success', maxi=maxi, mini=mini))

# fetch data by pymongo, generate a json file
# connect to local database
client = MongoClient('mongodb://localhost:27017')
db = client.moonquake
collection = db.moonquakes

# show the data on the website
@app.route('/success/<mini>/<maxi>')
def success(mini, maxi):
    data_list = []
    for moonquake in collection.find({"$and": [{"time_cmp": {"$lte": maxi}}, {"time_cmp": {"$gte": mini}}]}):
        data_list.append(moonquake)
    print(data_list)
    return render_template('fetchdata.html', data_list=data_list, mini=mini, maxi=maxi)
    # return 'Time span : {} => {}'.format(mini, maxi)

if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
