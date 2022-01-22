# Garantindo o intervalo correto, e corrigindo conforme a necessidade

import pandas as pd 
import datetime as dt

ride_sharing = pd.read_csv("C:/Users/lucasMartins/Documents/DataCamp/Cleaning Data/ride_sharing_new.csv")

# Intervalo int

# Convert tire_sizes to integer
ride_sharing['tire_sizes'] = ride_sharing['tire_sizes'].astype('int')

# Set all values above 27 to 27
ride_sharing.loc[ride_sharing["tire_sizes"] > 27,"tire_sizes"] = 27

# Reconvert tire_sizes back to categorical
ride_sharing['tire_sizes'] = ride_sharing["tire_sizes"].astype("category")

# Print tire size description
print(ride_sharing['tire_sizes'].describe())

# Intervalo date

# Convert ride_date to datetime
ride_sharing['ride_dt'] = pd.to_datetime(ride_sharing['ride_date'])

# Save today's date
today = dt.date.today()

# Set all in the future to today's date
ride_sharing.loc[ride_sharing['ride_dt'] > today, 'ride_dt'] = today

# Print maximum of ride_dt column
print(ride_sharing['ride_dt'].max())