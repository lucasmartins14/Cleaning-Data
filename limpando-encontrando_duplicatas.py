# Éncontrando dados duplicados

import pandas as pd 

ride_sharing = pd.read_csv("C:/Users/lucasMartins/Documents/DataCamp/Cleaning Data/ride_sharing_new.csv")

# Find duplicates
duplicates = ride_sharing.duplicated(subset = "ride_id", keep=False)

# Sort your duplicated rides
duplicated_rides = ride_sharing[duplicates].sort_values('ride_id')

# Print relevant columns of duplicated_rides
print(duplicated_rides[['ride_id','duration','user_birth_year']])