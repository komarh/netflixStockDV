#!/usr/bin/env python
# coding: utf-8

# In[2]:


from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns


# In[ ]:


netflix_stocks = pd.read_csv('NFLX.csv')
dowjones_stocks = pd.read_csv('DJI.csv')
netflix_stocks_quarterly = pd.read_csv(''NFLX_daily_by_quarter.csv'')


# #### Let’s load the datasets and inspect them.

# In[ ]:


print(netflix_stocks.head())
print(dowjones_stocks.head())
print(netflix_stocks_quarterly.head())


# #### Change the name of the column “Adj Close” to “Price” so that it is easier to work with the data.

# In[ ]:


netflix_stocks.rename(columns={"Adj Close":"Price"}, inplace=True)
netflix_stocks_quarterly.rename(columns={"Adj Close":"Price"}, inplace=True)
dowjones_stocks.rename(columns={"Adj Close":"Price"}, inplace=True)


# #### In this step, I will be visualizing the Netflix quarterly data!

# In[ ]:


ax = sns.violinplot(x="Quarter", y="Price", data=netflix_stocks_quarterly)
ax.set_title("Distribution of 2017 Netflix Stock Prices by Quarter")
ax.set_ylabel("Closing Stock Price")
ax.set_xlabel("Business Quarters in 2017")
plt.show()
plt.savefig("violin_nflx.png")


# #### Next, I will chart the performance of the earnings per share (EPS) by graphing the estimated Yahoo projected for the Quarter compared to the actual earnings for those quarters.

# In[ ]:


sns.set()
x_positions = [1, 2, 3, 4]
chart_labels = ["1Q2017","2Q2017","3Q2017","4Q2017"]
earnings_actual = [.4, .15, .29, .41]
earnings_estimate = [.37, .15, .32, .41]
plt.scatter(x_positions, earnings_actual, color="red", label="Actual")
plt.scatter(x_positions, earnings_estimate, color="blue", label="Estimate")
plt.legend()
plt.xticks(x_positions, chart_labels)
plt.title('Earnings Per Share in Cents')


# #### Next, I will visualize the earnings and revenue reported by Netflix by mapping two bars side-by-side.

# In[ ]:


#The metrics below are in billions of dollars
revenue_by_quarter = [2.79, 2.98, 3.29, 3.7]
earnings_by_quarter = [.0656, .12959, .18552, .29012]
quarter_labels = ["2Q2017", "3Q2017", "4Q2017", "1Q2018"]

#Revenue
n = 1
t = 2
d = 4
w = 0.8
bars1_x = [t*element + w*n for element in range(d)]

#Earnings
n = 2
t = 2
d = 4
w = 0.8
bars2_x = [t*element + w*n for element in range(d)]

middle_x = [ (a + b) / 2.0 for a, b in zip(bars1_x, bars2_x)]
labels = ["Revenue", "Earnings"]
plt.bar(bars1_x, revenue_by_quarter)
plt.bar(bars2_x, earnings_by_quarter)
plt.legend(labels)
plt.title("Earnings and Revenue Reported")
plt.xticks(middle_x, quarter_labels)
plt.show()


# #### In this last step, I will compare Netflix stock to the Dow Jones Industrial Average in 2017. I will accomplish this by plotting two line charts side by side in one figure.

# In[ ]:


#Left plot Netflix
fig = plt.figure(figsize = (13, 6))
ax1 = plt.subplot(1, 2, 1)
plt.plot(netflix_stocks["Date"], netflix_stocks["Price"], linestyle="--", marker="o",color="blue")
ax1.set_title("Netflix")
ax1.set_xlabel("Date")
ax1.set_ylabel("Stock Price")
plt.xticks(rotation=65, fontsize="x-small")

#Right plot Dow Jones
ax2 = plt.subplot(1, 2, 2)
plt.plot(dowjones_stocks["Date"], dowjones_stocks["Price"],linestyle="--", marker="o",color="blue")
ax2.set_title("Dow Jones")
ax1.set_xlabel("Date")
ax1.set_ylabel("Stock Price")
plt.xticks(rotation=65, fontsize="x-small")
plt.subplots_adjust(wspace=0.5)
plt.savefig("Comparison_Netflix&DJI.png")
plt.show()

