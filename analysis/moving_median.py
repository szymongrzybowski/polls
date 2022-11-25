import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

df = pd.read_csv('./polls19_date.csv')

x = pd.to_datetime(df.loc[:, "Fieldwork Period"])

y = df.loc[:, "United Right"]
y_smm = y.rolling(30).median()

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=120))
plt.gcf().autofmt_xdate()

plt.scatter(x, y, s=12, c='darkblue', alpha=0.28)
plt.plot(x, y_smm, c='darkblue', label="United Right")

plt.title("30-Period Moving Median; Oct 2019 – 5 Nov 2022")
plt.legend(loc='upper right', borderpad=0.25)
#plt.xticks(rotation=90)

plt.show()
