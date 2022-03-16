import datetime

def date():
  x = datetime.datetime.now()
  
  res = "Dziś jest "+x.strftime("%A")+" "+x.strftime("%m %B")

  return res
