import pandas as pd

def test_run():
	start_date='2010-01-22'
	end_date='2017-01-26'
	dates=pd.date_range(start_date,end_date)

	#Sets the date as the index
	df1=pd.DataFrame(index=dates)

	#Reads csv file with Date as the index and uses 3 columns, ignoring NaN
	dfSPY=pd.read_csv("data/SPY.csv",index_col='Date',parse_dates=True,usecols=['Date','Adj Close', 'Close'],na_values=['NaN'])

	#Joins only the dates provided in the date range
	df1=df1.join(dfSPY)
	
	#Drops NaN
	df1=df1.dropna()
	print df1

if __name__ == "__main__":
	test_run()

