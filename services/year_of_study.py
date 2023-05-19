#!/venv/bin python

NAMES = ["-",
  "Senior",
  "Junior",
  "Sophomore",
  "Freshmen",
  "Preparatory"]
from datetime import datetime
def get_graduation_year(name):
    year = datetime.now().year
    month = datetime.now().month    
    if month<9: year=year-1
    return year+NAMES.index(name)
