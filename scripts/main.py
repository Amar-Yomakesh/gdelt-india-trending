import extract_gdelt as gdelt
import pandas as pd
import aws_services as aws
from datetime import datetime

for theme in gdelt.config["themes"]:
    pd = gdelt.extract_gdelt_bytheme(theme)
    key = "files/"+datetime.now().strftime("%Y-%m-%d")+"_"+theme+".csv"
    aws.writeToS3(pd, key)
