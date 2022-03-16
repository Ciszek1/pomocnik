import requests

def weather():
  r = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=54.3290171&lon=18.5964206&appid=50d25bbab013b3251462733786b007d7')
  req = r.json()
  return "Aktualnie jest "+str(int(req["main"]["temp"])-273)+" stopni celciusza, wilgotność wynosi "+str(req["main"]["humidity"])+"%"
