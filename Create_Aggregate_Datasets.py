import requests
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from CallAPIs import *
from Clean_Orig_Data import *

# Create street segment dataframe using common key
cam_streets = pd.DataFrame(trafcam_df.STREETSEGID.unique())
safety_streets = pd.DataFrame(safety_df.STREETSEGID.unique())
bike_r_streets = pd.DataFrame(bike_r_df.STREETSEGID.unique())
crashes_streets = pd.DataFrame(crashes_df.STREETSEGID.unique())

streets_df = pd.merge(crashes_streets,
                       pd.merge(bike_r_streets,
                                pd.merge(cam_streets,
                                         safety_streets,
                                         how = 'outer'),
                                how = 'outer'),
                      how = 'outer').rename(columns = {0: "STREETSEGID"})

# Add number of traffic cams per street segment ID
streets_df['TRAFFIC_CAM'] = streets_df.apply(lambda _: 0, axis=1)
for index, val in enumerate(streets_df.STREETSEGID):
    if val in trafcam_df.STREETSEGID:
        streets_df.TRAFFIC_CAM[index] += 1


# Add number of safety concerns per street segment ID
safety_df_c = pd.DataFrame(safety_df.STREETSEGID.value_counts()).reset_index()
safety_df_c = safety_df_c.rename(columns = {'index' : 'STREETSEGID',
                                            'STREETSEGID' : 'SAFETY_CONCERNS'})

streets_df = streets_df.merge(safety_df_c, on = ['STREETSEGID'], how = 'outer')
streets_df = streets_df.drop_duplicates('STREETSEGID')

# Add number of safety concern issue type per street segment ID
# sum_issues_df = safety_df.groupby('STREETSEGID').count().reset_index()

for request_type in safety_df.REQUESTTYPE.unique():
    streets_df[request_type] = streets_df.apply(lambda _: 0, axis=1)
    for ind3, val3 in enumerate(safety_df.STREETSEGID):
        if val3 in streets_df.STREETSEGID and safety_df.REQUESTTYPE[ind3] == request_type:
            streets_df[request_type][ind3] += 1

# Add ward for each street segment
# Only two original datasets contain ward info for street segments
bike_r_df_ward = bike_r_df[['WARD', 'STREETSEGID']]
crashes_df_ward = crashes_df[['WARD', 'STREETSEGID']]
ward_df = bike_r_df_ward.merge(crashes_df_ward, on = ['STREETSEGID', 'WARD'], how = 'outer')

# Clean ward name nomenclature
ward_df.WARD = ward_df.WARD.replace({'Ward 5' : 5, '5':5, 'Ward 2' : 2, '2':2, 'Ward 6' : 6,
                                   '6':6, 'Ward 7' : 7, '7':7, 'Ward 8' : 8, '8' : 8,
                                   'Ward 4' : 4, '4' : 4, 'Ward 1' : 1, '1':1,
                                   'Ward 3' :  3, '3' : 3, 'Null' : 0})

streets_df = streets_df.merge(ward_df, on = 'STREETSEGID', how = 'outer')
streets_df = streets_df.drop_duplicates('STREETSEGID')

# Add value for each bike route associated with a street segment
bike_r_df_r = pd.DataFrame(bike_r_df.STREETSEGID.value_counts()).reset_index()
bike_r_df_r = bike_r_df_r.rename(columns = {'index' : 'STREETSEGID',
                                            'STREETSEGID' : 'BIKE_R'})

streets_df = streets_df.merge(bike_r_df_r, on = ['STREETSEGID'], how = 'outer')
streets_df = streets_df.drop_duplicates('STREETSEGID')


# Add value for each accident characteristic per street segment
sum_cols_df = crashes_df.groupby(['STREETSEGID']).sum().reset_index()

sum_cols_df = sum_cols_df[['STREETSEGID','MAJORINJURIES_BICYCLIST',
                          'MINORINJURIES_BICYCLIST', 'UNKNOWNINJURIES_BICYCLIST',
                          'FATAL_BICYCLIST', 'MAJORINJURIES_DRIVER', 'MINORINJURIES_DRIVER',
                          'UNKNOWNINJURIES_DRIVER', 'FATAL_DRIVER', 'MAJORINJURIES_PEDESTRIAN',
                          'MINORINJURIES_PEDESTRIAN', 'UNKNOWNINJURIES_PEDESTRIAN',
                          'FATAL_PEDESTRIAN', 'TOTAL_VEHICLES', 'TOTAL_BICYCLES',
                          'TOTAL_PEDESTRIANS', 'PEDESTRIANSIMPAIRED', 'BICYCLISTSIMPAIRED',
                          'DRIVERSIMPAIRED', 'TOTAL_TAXIS', 'TOTAL_GOVERNMENT',
                          'SPEEDING_INVOLVED', 'FATALPASSENGER', 'MAJORINJURIESPASSENGER',
                          'MINORINJURIESPASSENGER', 'UNKNOWNINJURIESPASSENGER']]

streets_df_trim = streets_df.merge(sum_cols_df, on = 'STREETSEGID', how = 'inner')
streets_df = streets_df.merge(sum_cols_df, on = 'STREETSEGID', how = 'outer')

# Clean the dataset! Impute null values as zero? or trim dataset?
streets_df_trim.fillna(0, inplace=True)
streets_df.fillna(0, inplace=True)

totals_df = pd.DataFrame(streets_df.sum()).reset_index()
totals_df = totals_df.rename(columns = {'index' : 'REPORT', 0 : 'COUNT'}).drop([0], axis = 0)

totals_by_ward_df = streets_df.groupby('WARD').sum().reset_index()
