import requests
import xmltodict

Station_URL = "http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByCodeXML?StationCode="
#Station_URL="http://api.irishrail.ie/realtime/realtime.asmx/getStationDataByNameXML?StationDesc="

search_URL = "http://api.irishrail.ie/realtime/realtime.asmx/getStationsFilterXML?StationText="

#Aux Vars
thisdict = {}
cleanData = {}

#gets raw data from Api
def getAPI(station):
  if station == None:
    station = "KBRCK"

  response = requests.get(Station_URL + station)

  return xmltodict.parse(response.content)


#Filters Station Data (dict_data)
def formatData(dict_data):

  print(len(dict_data["ArrayOfObjStationData"]))
  
  data = dict_data["ArrayOfObjStationData"]["objStationData"]

  next_trains_inStation = [row for row in data if is_valid_Duein(row["Duein"]) <= 30]

  return next_trains_inStation
  

def is_valid_Duein(Duein_String):

  try:
    return int(Duein_String)
  except:
    return False


def getStationNames(searchTxt):
  print(search_URL + searchTxt)
  response = requests.get(search_URL + searchTxt)

  try:
    parsedResponse = xmltodict.parse(response.content)
    data = parsedResponse['ArrayOfObjStationFilter']['objStationFilter']

  except:
    print("error")
    data = None
  
  return data