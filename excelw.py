import openpyxl
path = "Book1.xlsx"
excelwb_obj = openpyxl.load_workbook(path)
excelsheet = excelwb_obj.active
excelcell = excelsheet.cell(row=3, column=3)
print(excelcell.value)