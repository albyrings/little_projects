import requests
import geopandas as gpd
import matplotlib.pyplot as plt


ip = input("inserisci l'ip da cercare: ")
url_1 = "http://ipwhois.app/json/"
url = url_1 + ip
r = requests.get(url)
status_code = r.status_code
if status_code == 200:
    print('Connessione avvenuta con successo')
json = r.json()
print(json)
print('Il suo cliente si trova in questo luogo:', json['city'])

df = {
    'latitude': [float(json['latitude']),
                 float(json['latitude'])],
    'longitude': [float(json['longitude']),
                  float(json['longitude'])]
}
print(df)

world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

gdf = gpd.GeoDataFrame(
    df, geometry=gpd.points_from_xy(df['longitude'], df['latitude']))

ax = world.plot(color='peru', edgecolor='black')
plt.title('Posizione dei nostri clienti')
plt.xlabel('Longitudine')
plt.ylabel('Latitudine')
gdf.plot(ax=ax, color='yellow')
plt.show()
