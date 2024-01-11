import pandas as pd


df_bookings = pd.read_csv("C:\\Users\\USER\\Desktop\HDA\\datasets\\fact_bookings.csv")
df_date = pd.read_csv("C:\\Users\\USER\\Desktop\HDA\\datasets\\dim_date.csv")
df_hotels = pd.read_csv("C:\\Users\\USER\\Desktop\HDA\\datasets\\dim_hotels.csv")
df_rooms = pd.read_csv("C:\\Users\\USER\\Desktop\HDA\\datasets\\dim_rooms.csv")
df_agg_bookings = pd.read_csv("C:\\Users\\USER\\Desktop\\HDA\\datasets\\fact_aggregated_bookings.csv")





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

df_bookings = df_bookings[df_bookings.no_guests>0]
#restoring in same data frame, to exclude every booking with no guests (possibly errors)

avg, std = df_bookings.revenue_generated.mean(), df_bookings.revenue_generated.std()
#getting mean and standard deviation

#setting a possible limit of ravenue generated by a single booking, using common sense:
higher_limit = avg + 3*std 

lower_limit = avg - 3*std
#minimum ravenue as well

df_bookings[df_bookings.revenue_generated < 0]
#checking for errors - if revenue below 0 (impossible)

df_bookings = df_bookings[df_bookings.revenue_generated < higher_limit]

df_bookings = df_bookings[df_bookings.revenue_generated > lower_limit]
#putting df as lower then higer limit and higher than lower



df_bookings.revenue_realized.describe()

df_bookings.isnull().sum()


df_agg_bookings["occ_pct"] = df_agg_bookings["successful_bookings"] / df_agg_bookings["capacity"]
#making a column with occupation %



df_agg_bookings["occ_pct"] = df_agg_bookings["occ_pct"].apply(lambda x: round(x*100, 2))
df_agg_bookings.head()

#avg occupancy in each of room categories


df_agg_bookings.groupby("room_category")["occ_pct"].mean()
#RT1    58.224247
#RT2    58.040278
#RT3    58.028213
#RT4    59.300461

df_occ_room = pd.merge(df_agg_bookings, df_rooms, left_on="room_category", right_on="room_id")

print(df_occ_room.groupby("room_class")["occ_pct"].mean())
#Elite           58.040278
#Premium         58.028213
#Presidential    59.300461
#Standard        58.224247

#avg occupancy rare per city

df_occ_city = pd.merge(df_occ_room, df_hotels, on="property_id")

df_occ_city.groupby("city")["occ_pct"].mean().plot(kind="bar")

#Bangalore    56.594207
#Delhi        61.606467
#Hyderabad    58.144651
#Mumbai       57.936305

#when was the occupancy better? Weekend vs weekday

df = pd.merge(df_occ_city, df_date, left_on = "check_in_date", right_on="date")
df.head(3)

df.groupby("day_type")["occ_pct"].mean().round(2)
#weekeday    50.90
#weekend     72.39

#occupancy in different cities in June:

df_june_22 = df[df["mmm yy"] == "Jun 22"]

df_june_22.groupby("city")["occ_pct"].mean().round(2).sort_values()
#Bangalore    56.58
#Mumbai       58.38
#Hyderabad    58.46
#Delhi        62.47

#appending new data frame
df_august = pd.read_csv("C:\\Users\\USER\\Desktop\\HDA\\datasets\\new_data_august.csv")

latest_df = pd.concat([df, df_august], ignore_index=True, axis=0)











# print(df_bookings)