import pandas as pd

#This line reads in the Data.csv and parses the data into the YYYY-MM-DD format
data = pd.read_csv('/Jon/sd_pyds_a01/Data.csv', parse_dates=[0])

print (data)

#This line replaces the empty lines with the mean of the data set
fixed = data.fillna(data.mean())

print (fixed)

#Creating a DataFrame with a series of Countries and their capitals
toOutput = pd.DataFrame({'Country': pd.Series(['Canada','United States','Mexico','Brazil','United Kingdom']),'Capital':pd.Series(['Ottawa','Washington','Mexico City','Brazilia','London'])})
toOutput = toOutput[['Country','Capital']]

print(toOutput)

#This line writes the data set to Output.csv without an index
toOutput.to_csv('/Jon/sd_pyds_a01/Output.csv',index=False)

