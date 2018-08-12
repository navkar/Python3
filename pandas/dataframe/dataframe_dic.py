import pandas as pd
import numpy as np

cities = ['Austin', 'Dallas', 'Austin', 'Dallas']
signups = [7, 12, 3, 5]
visitors = [139, 237, 326, 456]
weekdays = ['Sunday', 'Sunday', 'Monday', 'Monday']
list_labels = ['city', 'signups', 'visitors', 'weekday']
list_cols = [cities, signups, visitors, weekdays]

zipped =  list(zip(list_labels, list_cols))

print("zipped...")
print(zipped)

data = dict(zipped)
users = pd.DataFrame(data)
print("---- Data frame ---")
print(users)
print("---- Data frame ---")