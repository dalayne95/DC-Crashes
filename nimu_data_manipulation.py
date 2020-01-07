from CallAPIs import *
from Clean_Orig_Data import *
from Create_Aggregate_Datasets import *

from scipy import stats
import numpy as np


safety_by_ward_df = totals_by_ward_df[['WARD', 'SAFETY_CONCERNS']]
safety_by_ward_df = safety_by_ward_df[1:9]

bike_route_info_df = streets_df.groupby('BIKE_R').sum().reset_index()
bike_route_info_df = bike_route_info_df[['SAFETY_CONCERNS', 'TOTAL_VEHICLES', 'TOTAL_BICYCLES', 'TOTAL_PEDESTRIANS']]
bike_route_info_df = bike_route_info_df.rename(index = {0:'Non Bike Route', 1: 'Bike Route'})

trafcam_info_df = streets_df.groupby('TRAFFIC_CAM').sum().reset_index()
trafcam_info_df = trafcam_info_df[['SAFETY_CONCERNS', 'Speeding', 'SPEEDING_INVOLVED', 'TOTAL_VEHICLES', 'TOTAL_BICYCLES', 'TOTAL_PEDESTRIANS']]
trafcam_info_df = trafcam_info_df.rename(index = {0:'No Traffic Camera', 1: 'Traffic Camera'})

safety_accid_by_ward_df = totals_by_ward_df[['WARD', 'SAFETY_CONCERNS', 'TOTAL_VEHICLES', 'TOTAL_PEDESTRIANS' ]]
safety_accid_by_ward_df = safety_accid_by_ward_df[1:9]




