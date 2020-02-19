# Title: Traffic Safety in Washington, D.C.

## Contributors:
- [Darian Madere](https://github.com/dalayne95)
- [Nimu Sidhu](https://github.com/gksidhu)

## Goals:
The goal of this analysis is to gain a better understanding of factors influencing the number of traffic accidents, injuries, and safety concern reports in Washington, D.C. Specifically, we tested whether ward, traffic cameras, and bike routes have a significant association with traffic safety.

## Data Sources
We used [Open Data DC](https://opendata.dc.gov/) to source the following four datasets:

* [Crashes in DC](https://opendata.dc.gov/) contains location, injury, and fatality information per traffic accident.
* [Vision Zero Safety](https://opendata.dc.gov/datasets/vision-zero-safety/) contains traffic safety reports from DC residents, including location and type of safety concern.
* [Traffic Cameras](https://opendata.dc.gov/datasets/traffic-camera/) contains traffic camera locations in DC.
* [Signed Bike Routes](https://opendata.dc.gov/datasets/signed-bike-routes/data) contains bike route locations in DC.

## Statistical Tests
The data sources used in this analysis report nominal data on traffic accidents and residents’ safety concerns. We aggregate this data as frequency information per street segment ID, or block, and per ward. In this aggregate data, the sample sizes are unequal, as some blocks and wards experience more traffic safety issues. Provided these two limitations, a non-parametric test or distribution-free statistic is most appropriate for our analysis. We have selected the Chi-square test as our non-parametric statistic of choice.

## Summary of Files: 
- [Slide Deck](https://github.com/dalayne95/DC-Crashes/blob/master/Presentation/Traffic%20Safety%20in%20DC.pdf)
- Data Sources
  - [Crashes in DC](https://opendata.dc.gov/datasets/crashes-in-dc/data)
  - [Vision Zero Safety](https://opendata.dc.gov/datasets/vision-zero-safety/)
  - [Traffic Cameras](https://opendata.dc.gov/datasets/traffic-camera)
  - [Signed Bike Routes](https://opendata.dc.gov/datasets/signed-bike-routes/data)
- Notebooks 
  - [Technical Notebook](https://github.com/dalayne95/DC-Crashes/blob/master/Notebooks/Technical_notebook.ipynb)
  - [Exploratory Data Analysis](https://github.com/dalayne95/DC-Crashes/blob/master/Notebooks/EDA.ipynb)
- Python files 
  - [API Calls](https://github.com/dalayne95/DC-Crashes/blob/master/Python_files/CallAPIs.py)
  - [Cleaning Data](https://github.com/dalayne95/DC-Crashes/blob/master/Python_files/Clean_Orig_Data.py)
  - [Combining Data for Analysis](https://github.com/dalayne95/DC-Crashes/blob/master/Python_files/Create_Aggregate_Datasets.py)
