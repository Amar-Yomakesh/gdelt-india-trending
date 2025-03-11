from datetime import datetime, timedelta
from gdeltdoc import GdeltDoc, Filters
from os import path
import yaml
import requests

# for running in jupiter notebook
configFile = path.abspath(path.join(__name__, "../../config/config.yaml"))
# configFile = "config/config.yaml"
try:
    with open(f'{configFile}', 'r') as f:
        config = yaml.safe_load(f)
except:
    print("config file not be loaded. exiting")
    exit(0)


def themes_lookup():
    theme_config = config['gdelt_api']["themes"]
    if theme_config["lookup"] is True:
        themesUrl = theme_config['url']
        result = requests.get(themesUrl).content
        result = result.decode(encoding="utf-8")
        themes = []
        for lines in result.split('\n'):
            themes.append(lines.split('\t')[0])
        return themes
    else:
        return theme_config["standardThemes"]


def getFilters(theme):
    current_date = datetime.now()
    f = Filters(
        country="IN",
        start_date=(current_date - timedelta(days=1)).strftime("%Y-%m-%d"),
        end_date=current_date.strftime("%Y-%m-%d"),
        theme=theme
    )
    return f


def extract_gdelt_timeline_bytheme(theme):
    gd = GdeltDoc()
    filter = getFilters(theme)
    return gd.timeline_search("timelinevolraw", filter)


def extract_gdelt_articles(theme):
    gd = GdeltDoc()
    filter = getFilters(theme)
    return gd.article_search(filter)
