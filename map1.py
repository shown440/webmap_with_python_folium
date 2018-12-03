import folium
import pandas

data = pandas.read_csv("VolcanoesUSA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def colorProducer(elevation):
    if elevation<1000:
        return "red"
    elif 1000<=elevation<3000:
        return "blue"
    else:
        return "green"

map = folium.Map(location=[38.58, -99.09], zoom_start=3, tiles="Mapbox Bright")


fgVolcanoes = folium.FeatureGroup(name = "Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fgVolcanoes.add_child(folium.CircleMarker(location=[lt, ln], radius=6, popup=folium.Popup(str(el)+" m", parse_html=True), fill_color=colorProducer(el),
    color="grey", fill_opacity=0.7, fill=True))


fgPopulation = folium.FeatureGroup(name = "Population")

fgPopulation.add_child(folium.GeoJson(data = open("world.json", "r", encoding="utf-8-sig").read(),
style_function = lambda x: {"fillColor":"blue" if x["properties"]["POP2005"]<10000000
else "orange" if 10000000<=x["properties"]["POP2005"]<=50000000
else "red"}))
    #load world.json data in reading mode with appropriate encoding
    #use lambda function to set various color in various location

map.add_child(fgVolcanoes)
map.add_child(fgPopulation)
#LayerControl must be added after featureGroup otherwise It will not work
map.add_child(folium.LayerControl())
#LayerControl is used for controllin various layer of map

map.save("Map1.html")
