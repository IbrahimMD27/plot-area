from geopy.distance import geodesic

origin_pt = eval(input("Enter the origin lat,long:"))
end_pt = eval(input("Enter the end lat,long:"))

distance = geodesic(origin_pt,end_pt).meters

print(distance)

input("for hold our screen in default python exe file")