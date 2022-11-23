import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('./polls19_date.csv')

x = pd.to_datetime(df.loc[:, "Fieldwork Period"])

y = df.loc[:, "United Right"]
y_sma = y.rolling(30).mean() # 30-period moving average
y_pct = y_sma.pct_change(30)


plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=120))
plt.gcf().autofmt_xdate()

plt.plot(x, y_pct, c='darkblue', label="United Right")
plt.title("Pct. Change of 30-Period Moving Average; Oct 2019 – 5 Nov 2022")
plt.legend(loc='upper right', borderpad=0.25)

plt.show()
