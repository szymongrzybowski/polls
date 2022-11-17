import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('./polls19_date.csv')

x = pd.to_datetime(df.loc[:, "Fieldwork Period"])

y = df.loc[:, "United Right"]
y_sma = y.rolling(30).mean()

y2 = df.loc[:, "Civic Coalition"]
y_sma2 = y2.rolling(30).mean()

y3 = df.loc[:, "The Left"]
y_sma3 = y3.rolling(30).mean()

y4 = df.loc[:, "Polish Coalition"]
y_sma4 = y4.rolling(30).mean()

y5 = df.loc[:, "Confederation"]
y_sma5 = y5.rolling(30).mean()

y6 = df.loc[:, "Poland 2050"]
y_sma6 = y6.rolling(30).mean()

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=120))
plt.gcf().autofmt_xdate()

plt.scatter(x, y_sma, s=11, c="darkblue")
plt.plot(x, y_sma, c="darkblue", label="United Right")

plt.scatter(x, y_sma2, s=11, c="orange")
plt.plot(x, y_sma2, c="orange", label="Civic Coalition")

plt.scatter(x, y_sma3, s=11, c="red")
plt.plot(x, y_sma3, c="red", label="The Left")

plt.scatter(x, y_sma4, s=11, c="green")
plt.plot(x, y_sma4, c="green", label="Polish Coalition")

plt.scatter(x, y_sma5, s=11, c="black")
plt.plot(x, y_sma5, c="black", label="Confederation")

plt.scatter(x, y_sma6, s=11, c="yellow")
plt.plot(x, y_sma6, c="yellow", label="Poland 2050")

#plt.xticks(rotation=90)
plt.title("30-Period Moving Average; Oct 2019 – 5 Nov 2022")

plt.legend(loc='upper right', borderpad=0.25)
plt.show()
