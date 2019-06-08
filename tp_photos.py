# Objectif : classer les photos qui sont sur Mayotte ou non

import exif
import folium

def add_marker(map, name, location):
  folium.Marker(
    location=location,
    popup=name,
    icon=folium.Icon(icon='picture')
  ).add_to(m)

# liste avec uniquement les photos situees a Mayotte
liste_mayotte = []

# pour les 3 photos
for index in range(3):
  photo = "photos/photo{}.jpg".format(index)
  # latitude et longitude de la photo
  lat = exif.latitude(photo)
  lon = exif.longitude(photo)

  # affiche les coordonnees si elles existent
  if lat == None or lon == None:
 	  print(photo, "Pas de coordonnées géographiques pour cette photo.")
  else:
    print(photo, lat, lon)
    # si les coordonnees correspondent a Mayotte
    if lat > -13.2 and lat < -12.5 and lon > 44.9 and lon < 45.4:
      liste_mayotte.append((photo, [lat, lon]))

print("Nombre de photos à Mayotte :", len(liste_mayotte))

m = folium.Map(location=[-12.83,45.15], zoom_start=11)

for photo in liste_mayotte:
  add_marker(m, photo[0], photo[1])

m.save('map.html')
