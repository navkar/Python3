import pandas as pd

heights = [59.0, 65.2, 62.9, 45.6, 34.5]
data = { 'height': heights, 'sex': 'M'}
results = pd.DataFrame(data)
print(results)
