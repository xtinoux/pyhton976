# Objectif : classer les photos qui sont sur Mayotte ou non

import exif

# latitude et longitude de la photo
lat = exif.latitude("photos/photo2.jpg")
lon = exif.longitude("photos/photo2.jpg")

if lat == None or lon == None:
  print("Pas de coordonnées géographiques pour cette photo.")
else:
	print(lat, lon)
