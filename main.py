from pytrends.request import TrendReq
import seaborn as sns
from datetime import datetime

pytrends = TrendReq(hl='en-US', tz=240)

QRY_NAMES = "Boeing"

kw_list = [QRY_NAMES]

# pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
pytrends.build_payload(kw_list, cat=0, timeframe='2019-03-01 2019-03-11', geo='', gprop='')

data = pytrends.interest_over_time()

#data = pytrends.get_historical_interest(kw_list, year_start=2019, month_start=3, day_start=1, hour_start=0, year_end=2019, month_end=3, day_end=24, hour_end=12, cat=0, geo='', gprop='', sleep=0)

# data['time'] = data.index
data['time'] = ["/".join(str(dt).split(' ')[0].split('-')[-2:]) for dt in data.index]
print(["/".join(str(dt).split(' ')[0].split('-')[-2:]) for dt in data["time"]])
print(data[-10:])
sns_plot = sns.barplot(x = "time", y = QRY_NAMES, data=data[-10:])
fig = sns_plot.get_figure()
fig.savefig(QRY_NAMES + ".png")
print("done")