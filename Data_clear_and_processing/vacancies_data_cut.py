import xlwt, xlrd
from xlutils.copy import copy as xlcopy

source_filename = "Test.xls"
destination_filename = "new_vacs_preprocessed_0.1.xls"

read_book = xlrd.open_workbook(source_filename, on_demand=True)
read_sheet = read_book.get_sheet(0)
write_book = xlcopy(read_book)

write_sheet = write_book.get_sheet(0)
for i in range (1, 25000):
    string = read_sheet.cell_value(i, 10)
    arr = string.split('*')

    
    for i in arr:
        exp = ""
        other = ""
        if i.find('years') != -1:
            exp += i
        else:
            other += i
        try:
            write_sheet.write(i, 12, exp)
        except:
            write_sheet.write(i, 12, 0)
        
        try:
            write_sheet.write(i, 13, other)
        except:
            write_sheet.write(i, 13, 0)

        write_book.save(destination_filename)

        if (i % 100 == 0):
            print(i)







# vacs_preprocessed_0.1.xls
