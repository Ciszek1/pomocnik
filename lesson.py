import json
import datetime
all = json.loads('[ { "All": "Polski, Matematyka, Wos, Historia", "Start": "ósmej", "End": "pietnasta trzydzieści" }, {},{}, { "All": "dwa wuefy, informatyke, Religie, Fizyke, Polski, Niemcki i kończysz angielski", "Start": "ósma", "End": "pietnastej trzydzieści" } ]')
x = datetime.datetime.now()

def lesson():
  x = datetime.datetime.now()
  w = int(x.strftime("%w"))
  return "Lekcje zaczynasz o "+all[w]["Start"]+", masz "+all[w]["All"]+" o godzine "+all[w]["End"]
