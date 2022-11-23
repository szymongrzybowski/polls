from scipy.stats import skew
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('./polls19_date.csv')

x = df.loc[:, "United Right"]

sk = skew(x, axis=0, bias=False)
print(sk) # 0.59

#plt.style.use('ggplot')
plt.hist(x, bins=25, color = "darkblue", lw=0)
plt.title("United Right: histogram; Oct 2019 – 5 Nov 2022")
plt.xlabel("Values")
plt.ylabel("Frequency")

plt.show()
