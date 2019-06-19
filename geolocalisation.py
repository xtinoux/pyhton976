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
	data = img._getexif()
	if data:
		try:
			gpsinfo = data[34853]
			latitude = _convert_exifGPs_to_decimal(gpsinfo[2])
			if gpsinfo[1] == 'S':
				return -1*latitude
			return latitude
		except KeyError:
		  return None

def longitude(img_path):
	"""
	Fonction qui prend en paramètre le chemin d'une image
	et renvoie la longitude.

	:: entrée (str) : Chemin du vers la photo
	:: sortie (float) : Longitude décimale
	"""
	img = Image.open(img_path)
	data = img._getexif()
	if data:
		try:
			gpsinfo = data[34853]
			longitude = _convert_exifGPs_to_decimal(gpsinfo[4])
			if gpsinfo[3] == 'W':
				return -1*longitude
			return longitude
		except KeyError:
		  return None


if __name__ == '__main__':
	print(latitude('photos/photo0.jpg'))
	print(longitude('photos/photo0.jpg'))
