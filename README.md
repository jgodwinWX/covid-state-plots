# covid-state-plots
A quick plotter for COVID-19 cases by U.S. state. Could be easily adapted for countries, provinces, or other geographies.

The x-axis plots the number of days since a state's nth case (n can be set by the user by changing the case_limit variable). The y-axis is the total cumulative number of cases (using a log scale).

Disclaimer: This code is provided as is, and is subject to errors. I am not an expert in any biological field (I haven't taken a biology class since high school). I am a meteorologist by trade, but like playing with numbers. tl;dr use only for curiosity purposes, and not for anything important.

Data source for CSV: https://en.wikipedia.org/wiki/Template:2019%E2%80%9320_coronavirus_pandemic_data/United_States_medical_cases

I provided the CSV file so you can see what it looks like for easy import into a pandas dataframe.
