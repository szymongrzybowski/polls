import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('./polls19_date_2.csv')

x = pd.to_datetime(df.loc[:, "Fieldwork Period"])

not_na = df[df['Poland 2050'].notna()]
x2 = not_na['Fieldwork Period']
x2_dt = pd.to_datetime(x2)

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

pre_y = df.loc[:, "Poland 2050"]
y6 = pre_y.dropna()
y_sma6 = y6.rolling(30).mean()

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=120))
plt.gcf().autofmt_xdate()

plt.scatter(x, y, s=11, c="darkblue", alpha=0.27)
plt.plot(x, y_sma, c="darkblue", label="United Right")

plt.scatter(x, y2, s=11, c="orange", alpha=0.27)
plt.plot(x, y_sma2, c="orange", label="Civic Coalition")

plt.scatter(x, y3, s=11, c="red", alpha=0.27)
plt.plot(x, y_sma3, c="red", label="The Left")

plt.scatter(x, y4, s=11, c="green", alpha=0.27)
plt.plot(x, y_sma4, c="green", label="Polish Coalition")

plt.scatter(x, y5, s=11, c="black", alpha=0.27)
plt.plot(x, y_sma5, c="black", label="Confederation")

plt.scatter(x2_dt, y6, s=11, c="yellow", alpha=0.27)
plt.plot(x2_dt, y_sma6, c="yellow", label="Poland 2050")

#plt.xticks(rotation=90)
plt.title("30-Period Moving Average; Oct 2019 – 5 Nov 2022")
plt.legend(loc='upper right', borderpad=0.25)

plt.show()
