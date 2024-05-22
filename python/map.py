import folium
import polyline
from stravaApi import *

activities = request()
#print(activities[0])

map = folium.Map(location=[43.0722, -89.4008], zoom_start=14, control_scale=True)

for count, activity in enumerate(activities):
    encodedLine = activity["map"]["summary_polyline"]
    
    decodedLine = polyline.decode(encodedLine)

    if (len(decodedLine) > 0):
        folium.PolyLine(locations=decodedLine, color="orange", opacity=1).add_to(map)

map.save("index.html")