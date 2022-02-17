# importing the requests library
from functions import *
from File_Mgt import *
from flask import Flask, request, Blueprint, flash, Markup, redirect, render_template, url_for

app = Flask('app', template_folder='template')


@app.route('/train')
def hello_world():

    #call func to get API Data
    dict_data = getAPI()

    return formatData(dict_data)


@app.route('/test')
def getStationInfo(station):

    #call func to get API Data
    dict_data = getAPI(station)

    return formatData(dict_data)


@app.route('/')
def home():

    return render_template('index.html')


@app.route('/kilbarrack')
def render_kilbarrack():

    entries = getStationInfo("KBRCK")

    return render_template('stationInfo.html',
                           entries=entries)


@app.route('/clontarf')
def render_clontarf():

    entries = getStationInfo("CTARF")
    return render_template('stationInfo.html',
                           entries=entries)


@app.route('/filetest')
def fileTest():

    return test(getStationInfo("Clontarf Road"))



@app.route('/search')
def render_search():

  return render_template('searchStation.html')

@app.route('/action_Search', methods =["POST"])
def render_action_Search():
  
  searchTxt = request.form.get("station")

  stations = getStationNames(searchTxt)
  
  return render_template('searchStation.html', stations=stations)


 
@app.route('/getStation', methods =["GET"])
def render_getStation():

  StationName = request.args.get('station')

  entries = getStationInfo(StationName)

  return render_template('stationInfo.html',
                           entries=entries,
                           Station=StationName)


app.run(host='0.0.0.0', port=8080)
