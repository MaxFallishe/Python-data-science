#http://geojson.io - закинуть сюда получившую таблицу
import geopy
import pandas
from geopy.geocoders import Nominatim, GoogleV3

geolocator = Nominatim(user_agent="D:\Geolocation",timeout=1000)

def main():
    io = pandas.read_csv('census-historic-population-borough.csv', index_col=None, header=0, sep=",")

    geolocate_column = io['Area Name'].apply(geolocator.geocode)
    io['latitude'] = geolocate_column.apply(get_latitude)
    io['longitude'] = geolocate_column.apply(get_longitude)
    io.to_csv('geocoding-output.csv')


def get_latitude(x):
  return x.latitude

def get_longitude(x):
  return x.longitude





if __name__ == '__main__':
  main()

