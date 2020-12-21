import pandas as pd

forex = pd.read_csv('GBPUSD_M1.csv')
print(forex.head(10))
forex.to_csv('gbpusd/gbpusd_1102_1218', index=True)