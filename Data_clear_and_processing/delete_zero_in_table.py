import xlwt, xlrd
from xlutils.copy import copy as xlcopy


lines_count = 13800

source_filename = "Book_with_coord.xls"
destination_filename = "Book_without_zero.xls"
emptyfile = "Empty.xlsx"

read_book = xlrd.open_workbook(source_filename, on_demand=True)
read_sheet = read_book.get_sheet(0)
write_book = xlcopy(xlrd.open_workbook(emptyfile, on_demand=True))

write_sheet = write_book.get_sheet(0)



for i in range (1 ,lines_count):
    print(read_sheet.cell_value(i, 9))

    if read_sheet.cell_value(i, 9) != 0:
        for n in range(0 ,11):
           write_sheet.write(i, n, read_sheet.cell_value(i, n))
            
    write_book.save(destination_filename)
