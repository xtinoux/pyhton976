from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS



def _convert_exifGPs_to_decimal(value):
    """
    Fonction utilitaire pour convertir les  données GPS
    au format décimal

	:: entrée (tuple) : Tuple issue des données EXIF
	:: sortie (float) : Valeur décimale 
	"""
    d = value[0][0] / value[0][1]
    m = value[1][0] / value[1][1]
    s = value[2][0] / value[2][1]

    return d + (m / 60) + (s / 3600)


def latitude(img_path):
	"""
	Fonction qui prend en paramètre le chemin d'une image
	et renvoie la latidude en degré minute seconde.

	:: entrée (str) : Chemin du vers la photo
	:: sortie (float) : Latitude décimale 
	"""
	img = Image.open(img_path)
	gpsinfo = img._getexif()[34853]
	latitude = _convert_exifGPs_to_decimal(gpsinfo[2])
	if gpsinfo[1] == 'S':
		return -1*latitude
	return latitude


def longitude(img_path):
	"""
	Fonction qui prend en paramètre le chemin d'une image
	et renvoie la longitude.

	:: entrée (str) : Chemin du vers la photo
	:: sortie (float) : Longitude décimale 
	"""
	img = Image.open(img_path)
	gpsinfo = img._getexif()[34853]
	longitude = _convert_exifGPs_to_decimal(gpsinfo[4])
	if gpsinfo[3] == 'E':
		return -1*longitude
	return longitude


if __name__ == '__main__':
	print(latitude('photos/1.jpg'))
	print(longitude('photos/1.jpg'))
# lat_d = lat[0][0] + lat[1][0]/60 + lat[2][0] /(36*10**len(str(lat[2][0])))
# lon_d = lon[0][0] + lon[1][0]/60 + lon[2][0] /(36*10**len(str(lon[2][0])))
# print(lat_d)
# print(lon_d)


# m = folium.Map(location=[lat_d, lon_d])
# tooltip = 'Click me!'

# folium.Marker([lat_d, lon_d], popup='<img src="image.jpg" heigth="200px" width="150px"></img>', tooltip=tooltip).add_to(m)
# # folium.Marker([48.8798477, 2.3551638125000003], popup='<b>Timberline Lodge</b>', tooltip=tooltip).add_to(m)
# m.save("localisation.html")