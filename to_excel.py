from openpyxl import Workbook, load_workbook
from openpyxl.drawing.image import Image
import os

def to_excel(path, cell_no):
    ***Saves visualizations into an excel file***
    excel = 'sentiment_plots.xlsx'
    if os.path.exists(excel):
        workbook = load_workbook(excel)
    else:
        workbook = Workbook()
        workbook.active.title = "sentiment_plots"
    sheet = workbook.active

    #Insert image into the sheet
    img = Image(path)
    img.anchor = cell_no
    sheet.add_image(img)

    #Save excel file
    workbook.save(excel)os
