from datetime import datetime, timedelta
from gdeltdoc import GdeltDoc, Filters
import yaml

configFile = 'config/config.yaml'
try:
    with open(f'{configFile}', 'r') as f:
        config = yaml.safe_load(f)
except:
    print("config file not be loaded. exiting")
    exit(0)


def getFilters(theme):
    current_date = datetime.now()
    f = Filters(
        country="IN",
        start_date=(current_date - timedelta(days=1)).strftime("%Y-%m-%d"),
        end_date=current_date.strftime("%Y-%m-%d"),
        theme=theme
    )
    return f


def extract_gdelt_bytheme(theme):
    gd = GdeltDoc()
    filter = getFilters(theme)
    return gd.timeline_search("timelinevolraw", filter)
