import pandas as pd


df_bookings = pd.read_csv("C:\\Users\\USER\\Desktop\HDA\\datasets\\fact_bookings.csv")
df_date = pd.read_csv("C:\\Users\\USER\\Desktop\HDA\\datasets\\dim_date.csv")
df_hotels = pd.read_csv("C:\\Users\\USER\\Desktop\HDA\\datasets\\dim_hotels.csv")
df_rooms = pd.read_csv("C:\\Users\\USER\\Desktop\HDA\\datasets\\dim_rooms.csv")
df_agg_bookings = pd.read_csv("C:\\Users\\USER\\Desktop\HDA\\datasets\\fact_aggregated_bookings.csv")





print(df_bookings.shape)
#tells how many rows/colums are in data frame

print(df_bookings.room_category.unique())
#shows unique rooms category

print(df_bookings.booking_platform.unique())
#shows unique booking_platform are there

print(df_bookings.booking_platform.value_counts())
#shows number of bookings made by particular booking platform

print(df_bookings.describe())
#statistics for columns

print(df_hotels.city.value_counts())
#shows how many hotels are in particular cities



# print(df_bookings)