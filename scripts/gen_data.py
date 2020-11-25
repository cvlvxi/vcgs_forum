import pandas as pd
from typing import List
from datetime import datetime
import random
import csv

num_periods = 1261
datelist: List[pd.Timestamp] = pd.date_range(start=datetime(year=2020, month=3, day=10), end=datetime.today(), periods=num_periods).tolist()
datelist = [f"{x.year}-{x.month}-{x.day}" for x in datelist]

def gen_random_vals(num_periods, start = 30, add_amount = 10, intervals = 1000) -> List[float]:
    # Generate random numbers
    end = start + add_amount
    traverse_intervals = round(num_periods / intervals)

    curr_interval = 1
    result = []
    for i in range(num_periods):
        result.append(random.uniform(start, end))
        if i % traverse_intervals == 0:
            curr_interval += 1
            start = start + add_amount
            end = end + add_amount
    return result

_open =  gen_random_vals(num_periods, start=random.uniform(10, 30), add_amount=random.uniform(10, 30), intervals=random.randint(500, 1000))
_high =  gen_random_vals(num_periods, start=random.uniform(10, 30), add_amount=random.uniform(10, 30), intervals=random.randint(500, 1000))
_low =  gen_random_vals(num_periods, start=random.uniform(10, 30), add_amount=random.uniform(10, 30), intervals=random.randint(500, 1000))
_close =  gen_random_vals(num_periods, start=random.uniform(10, 30), add_amount=random.uniform(10, 30), intervals=random.randint(500, 1000))
_adj_close = gen_random_vals(num_periods, start=random.uniform(10, 30), add_amount=random.uniform(10, 30), intervals=random.randint(500, 1000))
_volume = gen_random_vals(num_periods, start=random.uniform(36027600,46027600) , add_amount=random.uniform(400000, 700000), intervals=random.randint(500, 1000))

with open("LeftHanded.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(["Date", "Open", "High", "Low", "Close", "Adj Close", "Volume"])
    for i in range(num_periods):
        data = [datelist[i], _open[i], _high[i], _low[i], _close[i], _adj_close[i], _volume[i]]
        writer.writerow(data)
