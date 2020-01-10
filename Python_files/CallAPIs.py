import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def create_df(url):
    response = requests.get(url)
    print('Response Status Code =', response.status_code)
    item_list = []
    for item in response.json()['features']:
        item_list.append(item['attributes'])
    df = pd.DataFrame(item_list, )
    return df

crashes_url = 'https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Public_Safety_WebMercator/MapServer/24/query?where=1%3D1&outFields=*&outSR=4326&f=json'
crashes_df = create_df(crashes_url)

trafcam_url = 'https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Transportation_WebMercator/MapServer/93/query?where=1%3D1&outFields=*&outSR=4326&f=json'
trafcam_df = create_df(trafcam_url)

safety_url = 'https://maps2.dcgis.dc.gov/dcgis/rest/services/DDOT/VisionZero/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json'
safety_df = create_df(safety_url)

bike_r_url = 'https://maps2.dcgis.dc.gov/dcgis/rest/services/DCGIS_DATA/Transportation_WebMercator/MapServer/6/query?where=1%3D1&outFields=*&outSR=4326&f=json'
bike_r_df = create_df(bike_r_url)
