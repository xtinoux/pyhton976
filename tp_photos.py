# Objectif : classer les photos qui sont sur Mayotte ou non

from  geolocalisation import *
import folium

def add_marker(my_map, name, location):
  """

  """
  folium.Marker(
    location=location,
    popup=f"<img src='{name}' alt='{name}' height=250px width=250px/>",
    icon=folium.Icon(icon='picture')
  ).add_to(my_map)


liste_photo = []

for i in range(0,571):
  photo = 'photos/photo{}.jpg'.format(i)
  lat = latitude(photo)
  lon = longitude(photo)

  if lat == None:
    print("Pas de coordonnées")
  else :
    print('Y a des coordonnées')
    if lat > -13.1 and lat < -12.5 and lon > 44.5 and lon < 45.5:
      print("La photo a été prise à Mayotte")
      liste_photo.append(photo)
print(liste_photo)


m = folium.Map(location=[-12.83,45.15], zoom_start=11)

for photo in liste_photo:
  add_marker(m, photo, (latitude(photo),longitude(photo)))

m.save('map.html')

