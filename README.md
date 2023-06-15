# Bike Share Analysis

This project analyzes bike share data for three cities: Chicago, New York City, and Washington. The provided dataset includes information about bike trips such as start time, end time, trip duration, start station, end station, user type, and additional information for Chicago and New York City including gender and birth year.

Provided in both .py and .ipynb formats

# Requirements

This projects assumes:
-Python 3.x installed
-pandas, numpy libraries installed
-chicago.csv, new_york_city.csv, washington.csv data files in the same directory due to hard coded pathing

#References

- official Pandas documentation
  https://pandas.pydata.org/docs/reference/api/pandas.Series.dt.day_name.html

the solution code in practice question 3 of the 'Explore US Bikeshare Data' lesson references the depreciated method '.dt.weekday_name', after referencing the documentation I found the updated method to be '.dt.day_name()'
