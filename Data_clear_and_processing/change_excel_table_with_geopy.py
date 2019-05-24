import xlwt, xlrd
from xlutils.copy import copy as xlcopy

from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="D:\Geolocation",timeout=1000)

source_filename = "Book1.xls"
destination_filename = "Book1_new.xls"

read_book = xlrd.open_workbook(source_filename, on_demand=True)

read_sheet = read_book.get_sheet(0)
write_book = xlcopy(read_book)

write_sheet = write_book.get_sheet(0)
for i in range (6838, 13800):
    print(read_sheet.cell_value(i, 1))
    location = geolocator.geocode(read_sheet.cell_value(i, 1))
    try:
        write_sheet.write(i, 9, location.latitude)
    except:
        write_sheet.write(i, 9, 0)
        
    try:
        write_sheet.write(i, 10, location.longitude)
    except:
        write_sheet.write(i, 10, 0)
    if (i % 100 == 0):
        print(i)
    write_book.save(destination_filename)
    
