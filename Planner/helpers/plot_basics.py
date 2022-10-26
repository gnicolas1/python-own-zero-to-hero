import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime as dt

start_date = dt.date(2022, 11, 1)
end_date = dt.date(2022, 11, 30)

Task = ['task1']
Task_Value = [(dt.date(2022, 11, 15) - dt.date(2022, 11, 10)).days]
Task_Offset = [dt.date(2022, 11, 10)]

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=7))

plt.barh(Task, Task_Value, 0.3, left=Task_Offset)
plt.xlim(start_date, end_date)
plt.show()
