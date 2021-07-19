import pandas as pd
import json
import folium
from folium import plugins
from folium.plugins import HeatMap

fn = "geodata.json"

df = pd.DataFrame(columns=['latitude','longitude','snr','rssi'])

with open(fn) as f:
    for line in f:
        try:
            chunks = line.partition('message received')
            gps = chunks[2]
            gps2 = gps.strip()
            #gps3 = gps2[1:]
            #gps4 = gps3[:-1]
            print(gps2)
            gps5 = json.dumps(gps2)
            d = json.JSONDecoder()
            entry = d.decode(gps2)
            message = entry['message']
            rssi = entry['rssi']
            snr = entry['snr']
            values = message.split(':')
            coords = values[4].split(',')
            lat = coords[0].replace('N',"")
            lon = coords[1].replace('W',"")
            alt = values[6]
            sats = values[8]

            entry = dict(latitude=lat,longitude=lon, snr=snr, rssi=rssi)
            df = df.append(entry, ignore_index=True)
        except:
            pass

    # Ensure you're handing it floats
    df['latitude'] = df['latitude'].astype(float)
    df['longitude'] = df['longitude'].astype(float)
    heat_df = df[['latitude', 'longitude']]
    heat_df = heat_df.dropna(axis=0, subset=['latitude', 'longitude'])
    # List comprehension to make out list of lists
    heat_data = [[row['latitude'], row['longitude']] for index, row in heat_df.iterrows()]

    map_hooray = folium.Map(location=[38.859882, 77.238976],
                            zoom_start=13)
    heat_data = heat_df.values.tolist()
    HeatMap(heat_data, radius=13).add_to(map_hooray)

    # Plot it on the map
    #HeatMap(heat_data).add_to(map_hooray)
