from datetime import datetime, timedelta
from gdeltdoc import GdeltDoc, Filters
from os import path
import yaml

configFile = path.abspath(path.join(__name__ ,"../../config/config.yaml"))
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

gd = GdeltDoc()


def extract_gdelt_timeline_bytheme(theme):
    filter = getFilters(theme)
    return gd.timeline_search("timelinevolraw", filter)

def extract_gdelt_articles():
    filter = getFilters(theme)
    return gd.article_search(filter)

