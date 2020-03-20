import datetime
import pandas
import matplotlib.pyplot as plt
import numpy

# user input
case_limit = 50

# import data
df = pandas.read_csv('covid_data.csv',index_col='Date').fillna(0).cumsum()
ref_date = datetime.datetime.strptime(df.index[-1],'%Y/%m/%d').date()

# remove states with less than case_limit cases
cols = (df >= case_limit).any()
df_new = df[cols[cols].index]

# get first date where cases exceeded 100
firstdate = {}
for col in df_new.columns:
	firstdate[col] = df_new[df_new[col] >= case_limit].index[0]

# convert the first dates to datetime objects
firstdates_dt = {}
firstdates_dt = {k: datetime.datetime.strptime(v,'%Y/%m/%d').date() for k,v in firstdate.items()}
dayssince = {}
dayssince = {k: (ref_date - v).days + 1 for k,v in firstdates_dt.items()}

# plot data

plt.clf()
fig,ax = plt.subplots(figsize=(12,8))
for col in df_new.columns:
	xdata = numpy.arange(0,dayssince[col])
	ydata = df_new[col][df_new[col] >= case_limit].values
	ax.plot(xdata,ydata,marker='o')
	ax.annotate(s=col,xy=(xdata[-1],ydata[-1]),xytext=(5,0),textcoords='offset points')

plt.yscale('log')
plt.grid(which='major',axis='both',ls='-')
		
# axis labels
plt.title('Confirmed COVID-19 Cases by State',fontsize=24)
plt.xlabel('Days since %.0f cases' % case_limit,fontsize=20)
plt.xticks(ticks=numpy.arange(0,21),labels=numpy.arange(0,21),fontsize=16)
plt.xlim([0,20])
plt.ylabel('Number of Cases',fontsize=20)
plt.yticks(fontsize=16)
plt.ylim([10,100000])
		
plt.savefig('cumulative_cases.png',bbox_inches='tight')