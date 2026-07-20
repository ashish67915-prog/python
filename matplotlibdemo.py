#import libraries
import numpy as np
import pandas  as pd
import matplotlib.pyplot as plt
import seaborn as sns

#2D line plot
# price = [54000,56000,60000,45000,44000,42000]
# year = [2017,2018,2019,2020,2021,2022]
# plt.plot(year,price)
# plt.title("sample graph")
# plt.show()

# batsman = pd.read_csv('C:/Users/ASHISH YADAV/OneDrive/Desktop/Python/csvfiles/sharma-kohli.csv')
# print(batsman)
# plt.plot(batsman['index'],batsman['V Kohli'],color='blue',linestyle='solid',linewidth=2,marker='D',label='virat')
# plt.plot(batsman['index'],batsman['RG Sharma'],color='yellow',linestyle='dotted',linewidth=1,marker='D',label='Rohit')
# plt.title("Virat Kohli and Rohit sharma progress")
# plt.xlabel("Season")
# plt.ylabel("Runs Scored")
# plt.legend()
# plt.show()


#case when some outliers comes then we use the concept limiting axes
#limiting axes
# price = [54000,56000,60000,45000,44000,42000,4500000]
# year = [2017,2018,2019,2020,2021,2022,2023]
# plt.plot(year,price)
# plt.title("sample graph")
# plt.ylim(0,75000)

# plt.show()



#scatter plot
# x = np.linspace(-10,10,50)
# y = 10*x + 3 + np.random.randint(0,300,50)
# plt.scatter(x,y)
# plt.show()

# df = pd.read_csv('C:/Users/ASHISH YADAV/OneDrive/Desktop/Python/csvfiles/batter.csv')
# plt.scatter(df['avg'],df['strike_rate'])
# plt.title("Average and Strike rate analysis")
# plt.xlabel('avg')
# plt.ylabel('strike_rate')
# plt.show()


#bar graph
# x = [5,10,15,20]
# y = ['red','white','yellow','blue']
# plt.bar(x,y)
# plt.show()


#multiple bars
# df = pd.read_csv('C:/Users/ASHISH YADAV/OneDrive/Desktop/Python/csvfiles/batsman_season_record.csv')
# plt.bar(np.arange(df.shape[0])-0.2,df['2015'],width=0.2)
# plt.bar(np.arange(df.shape[0]),df['2016'],width=0.2)
# plt.bar(np.arange(df.shape[0])+0.2,df['2017'],width=0.2)
# plt.xticks(np.arange(df.shape[0]),df['batsman'])
# plt.show()


#problem when more words  are give
# children = [10,20,40,10,30]
# colors =  ['red red red red red red','blue blue blue blue blue blue','yellow yellow yellow','black black black black black black black','green green green green']
# plt.bar(colors,children,color='blaCK')
# plt.xticks(rotation='vertical')
# plt.show()


# df = pd.read_csv('C:/Users/ASHISH YADAV/OneDrive/Desktop/Python/csvfiles/batsman_season_record.csv')
# plt.bar(df['batsman'],df['2017'],label='2017')
# plt.bar(df['batsman'],df['2016'],bottom=df['2017'],label='2016')
# plt.bar(df['batsman'],df['2015'],bottom=(df['2016'] + df['2017']),label='2015')
# plt.legend()
# plt.show()


#histogram
# df = pd.read_csv('C:/Users/ASHISH YADAV/OneDrive/Desktop/Python/csvfiles/vk.csv')
# plt.hist(df['batsman_runs'],bins=[10,20,30,40,50,60,70,80,90,100,110,120])
# plt.show()


#logarithmic scale
# df = np.load('C:/Users/ASHISH YADAV/OneDrive/Desktop/Python/csvfiles/big-array.npy')
# plt.hist(df,bins=[10,20,30,40,50,60,70],log=True)
# plt.show()



#pie chart
data = [23,40,100,75,80]
subjects = ['fomc','yoga','c++','phy','maths']
plt.pie(data,labels=subjects)
plt.show()