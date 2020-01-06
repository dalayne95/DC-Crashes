import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from CallAPIs import *

# Convert float64 date columns to timestamps
def unix_to_dtime(df_columnname):
    df_columnname = pd.to_datetime(df_columnname, origin = 'unix', unit = 'ms')
    return df_columnname

crashes_df.REPORTDATE = unix_to_dtime(crashes_df.REPORTDATE)
crashes_df.FROMDATE = unix_to_dtime(crashes_df.FROMDATE)
crashes_df.TODATE = unix_to_dtime(crashes_df.TODATE)
crashes_df.LASTUPDATEDATE = unix_to_dtime(crashes_df.LASTUPDATEDATE)

safety_df.REQUESTDATE = unix_to_dtime(safety_df.REQUESTDATE)

bike_r_df.UPDATETIME = unix_to_dtime(bike_r_df.UPDATETIME)

# Integrate traffic camera boolean column for each crash
crashes_df['TRAFFIC_CAM'] = crashes_df.apply(lambda _: '', axis=1)
for index, val in enumerate(crashes_df.STREETSEGID):
    if val in trafcam_df.STREETSEGID:
        crashes_df.TRAFFIC_CAM[index] = 1
    else:
        crashes_df.TRAFFIC_CAM[index] = 0
