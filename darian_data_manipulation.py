from CallAPIs import *
from Clean_Orig_Data import *
from Create_Aggregate_Datasets import *

from scipy import stats
import numpy as np

pd.options.display.max_columns = None
ward_accidents_df = crashes_df.groupby(["WARD"]).agg('count')

ward_accidents_df = ward_accidents_df.rename(columns={"OBJECTID": "incidents"})
ward_accidents_df = ward_accidents_df.drop(columns=['CRIMEID', 'CCN', 'REPORTDATE', 'ROUTEID', 'MEASURE', 'OFFSET', 'ROADWAYSEGID', 'FROMDATE', 'TODATE', 'MARID', 'ADDRESS', 'LATITUDE', 'LONGITUDE', 'XCOORD', 'YCOORD', 'EVENTID', 'MAR_ADDRESS', 'MAR_SCORE'])

ward_accidents = ward_accidents_df[['incidents']].copy()
ward_accidents = ward_accidents.drop(['Null'])


# Hypothesis #3
ward_count = crashes_df.groupby(['WARD']).agg('count')

ward_count = ward_count[['OBJECTID']].copy()
ward_count = ward_count.drop(['Null'])

injuries = crashes_df.groupby(['WARD']).agg('sum')

injuries['bike_total_injuries'] = injuries['MAJORINJURIES_BICYCLIST'] + injuries['MINORINJURIES_BICYCLIST'] + injuries['UNKNOWNINJURIES_BICYCLIST']                                       
injuries['driver_total_injuries'] = injuries['MAJORINJURIES_DRIVER'] + injuries['MINORINJURIES_DRIVER'] + injuries['UNKNOWNINJURIES_DRIVER']
injuries['pedestrian_total_injuries'] = injuries['MAJORINJURIES_PEDESTRIAN'] + injuries['MINORINJURIES_PEDESTRIAN'] + injuries['UNKNOWNINJURIES_PEDESTRIAN']

injuries = injuries[['pedestrian_total_injuries','bike_total_injuries','driver_total_injuries']]        

ward_injuries = pd.concat([ward_count, injuries], axis=1)
ward_injuries = ward_injuries.drop(['Null'])
ward_injuries = ward_injuries.rename(columns={"OBJECTID": "incidents"})

ward_injuries['total_injuries'] = ward_injuries['pedestrian_total_injuries'] + ward_injuries['bike_total_injuries'] + ward_injuries['driver_total_injuries']
ward_injuries = ward_injuries.drop(['incidents','pedestrian_total_injuries','bike_total_injuries','driver_total_injuries'], axis=1)
